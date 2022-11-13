import numpy as np
import tensorflow as tf
import tfrecorder

t_path='/home/tian_hy/Qsync/上海工程技术大学/毕业论文/程序/0 Data/TFRecorder/P_N.tfrecords'
img, label = tfrecorder.read_and_decode(t_path,N_CLASSES = 4, n_epochs=1) 
img, label = tf.train.batch([img, label], batch_size=4)
img = tf.cast(img, tf.float32)
with tf.Session() as sess:
    tf.local_variables_initializer().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    try:
        image = sess.run(img)
        print(image)

    except tf.errors.OutOfRangeError:
        print('Done testing -- epoch limit reached')
    
    finally:
       pass 