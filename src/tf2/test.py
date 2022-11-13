import sys, importlib, time
import numpy as np
import utils.data as data
import parameters.parameters2_1 as pm
import tensorflow.compat.v1 as tf

def main(sys):
    args = pm.parse_arguments(sys)
    network = importlib.import_module(args.model)

    with tf.Graph().as_default() :
        input, label = data.TFRecord_Batch(args.Test_TFRecord_dir, args.n_classes, args.test_n_epochs, args.batch_size, args.min_after_dequeue)

        predictions = network.inference(input, args.model_def, args.test_phase_train)
        total_loss = data.loss(predictions, label)
        accur = data.evaluation(predictions, label)

        with tf.Session() as sess:
            sess.run(tf.local_variables_initializer())
            saver = tf.train.Saver()

            print('Reading Checkpoint...')
            ckpt = tf.train.get_checkpoint_state(args.train_model_dir)
            print(ckpt.model_checkpoint_path)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                print('Loading success, global step is %s' % global_step)
            else:
                print('No checkpoint file found')

            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(sess=sess, coord=coord)

            start_time = time.time()
            final_accurate = 0
            final_loss = 0
            flag = 1
            time_point2 = time.time()

            try:
                for step in np.arange(args.max_step):
                    if coord.should_stop():
                        break
                    loss, acc = sess.run([total_loss, accur])
                    final_accurate = final_accurate + acc
                    final_loss = final_loss + loss
                    if step%50 == 0:
                        if flag == 1:
                            time_point1 = time.time()
                            flag = 0
                        else:
                            time_point2 = time.time()
                            flag = 1
                        print('Time =', round(abs(time_point2-time_point1), 2), 'secs, Step = %d, Accuracy = %.4f%%, Loss = %.4f' %(step, acc, loss))

            except tf.errors.OutOfRangeError:
                print('Done testing -- epoch limit reached')

            finally:
                end_time = time.time()
                final_accurate = final_accurate*100/step
                final_loss = final_loss/step
                print('Time =', round(end_time-start_time, 2), 'secs, Step = %d, Test loss = %.4f, Test accuracy = %.4f%%' %(step, final_loss, final_accurate))
                coord.request_stop()


if __name__=='__main__':
    main(sys.argv[1:])
