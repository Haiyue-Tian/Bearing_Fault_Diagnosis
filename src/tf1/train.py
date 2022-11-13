import sys, os, importlib, time
import numpy as np
import utils.data as data
import tensorflow as tf
import parameters.parameters2_1 as pm

def main(sys):
    args = pm.parse_arguments(sys)
    network = importlib.import_module(args.model)
    train_log_dir = args.train_log_dir
    train_model_dir = args.train_model_dir
    if not tf.gfile.Exists(train_log_dir):
        tf.gfile.MakeDirs(train_log_dir)
    if not tf.gfile.Exists(train_model_dir):
        tf.gfile.MakeDirs(train_model_dir)

    with tf.Graph().as_default() as graph:
        global_step = tf.Variable(0, trainable=False, name='global_step')
        input, label = data.TFRecord_Batch(args.TFRecord_dir, args.n_classes, args.n_epochs,
                                           args.batch_size, args.min_after_dequeue )

        predictions = network.inference(input, args.model_def, args.phase_train)
        total_loss = data.loss(predictions, label)
        accur = data.evaluation(predictions, label)
        optimizer =data.training(args.optimizer, args.learning_rate_parameters, global_step)
        train_op = optimizer.minimize(total_loss, global_step=global_step)

        summary_op = tf.summary.merge_all()

        with tf.Session(graph=graph) as sess:
            sess.run(tf.global_variables_initializer())
            saver = tf.train.Saver()
            train_writer = tf.summary.FileWriter(args.train_log_dir, sess.graph)

            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(sess=sess, coord=coord)

            start_time = time.time()
            point_time1 = time.time()
            flag = 1
            try:
                for step in np.arange(args.max_step):
                    if coord.should_stop():
                        break
                    _, batch_accuracy, batch_loss  = sess.run([train_op, accur, total_loss])
                    if step%10 == 0:
                        if flag:
                            point_time2 = time.time()
                            flag = 0
                        else:
                            point_time1 = time.time()
                            flag = 1
                        batch_time = round(abs(point_time1-point_time2))
                        print('Step %d, Time = %d sec, train loss = %.4f, train accuracy = %.4f%%' 
                              %(step, batch_time, batch_loss, batch_accuracy*100.0))
                        summary_str = sess.run(summary_op)
                        train_writer.add_summary(summary_str, step)
                    if step%100 == 0:
                        name_ckpt = args.name_ckpt[0:-5] + '_' + str(batch_loss) + args.name_ckpt[-5:]
                        checkpoint_path = os.path.join(train_model_dir, name_ckpt) #改名字，记时
                        saver.save(sess, checkpoint_path, global_step=step)

            except tf.errors.OutOfRangeError:
                print('Done training -- epoch limit reached')

            finally:
                end_time = time.time()
                print('Total_time = %.4f min' %(round(end_time-start_time)/60))
                coord.request_stop()
                train_writer.close()

if __name__ == '__main__':
    main(sys.argv[1:])
