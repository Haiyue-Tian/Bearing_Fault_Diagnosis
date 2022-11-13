import utils.tfrecorder as tfrecorder
import tensorflow as tf
import tf_slim as slim

def get_batch(input, label, batch_size, min_after_dequeue) :
    capacity = min_after_dequeue+3*batch_size
    data, label = tf.train.shuffle_batch([input, label],
                                         batch_size=batch_size, 
                                         num_threads=32, 
                                         capacity=capacity,
                                         min_after_dequeue=min_after_dequeue)
    data = tf.cast(data, tf.float32)
    return data, label

def TFRecord_Batch(tfrecorder_path, N_CLASSES, n_epochs, batch_size, min_after_dequeue):
    input, label = tfrecorder.read_and_decode(tfrecorder_path,  N_CLASSES, n_epochs = n_epochs)
    input, label = get_batch(input, label, batch_size, min_after_dequeue)
    return input, label

def loss(logits, label):
    with tf.variable_scope('losses') as scope:
        cross_entropy = slim.losses.softmax_cross_entropy(logits, label, scope='losses/x_entropy')
        total_loss = slim.losses.get_total_loss()
        tf.summary.scalar('losses/total_loss', total_loss)
    return total_loss

def training(optimizer, learning_rate_parameters, global_step):
    renew_learning_rate = learning_rate(learning_rate_parameters, global_step)
    # renew_learning_rate = 0.001
    with tf.name_scope('optimizer'):
        if optimizer=='ADAGRAD':
            opt = tf.train.AdagradOptimizer(renew_learning_rate)
        elif optimizer=='ADADELTA':
            opt = tf.train.AdadeltaOptimizer(renew_learning_rate, rho=0.9, epsilon=1e-6)
        elif optimizer=='ADAM':
            opt = tf.train.AdamOptimizer(renew_learning_rate, beta1=0.9, beta2=0.999, epsilon=0.1)
        elif optimizer=='RMSPROP':
            opt = tf.train.RMSPropOptimizer(renew_learning_rate, decay=0.9, momentum=0.9, epsilon=1.0)
        elif optimizer=='MOM':
            opt = tf.train.MomentumOptimizer(renew_learning_rate, 0.9, use_nesterov=True)
        else:
            raise ValueError('Invalid optimization algorithm')
    return opt

def evaluation(prediction, label):
    with tf.variable_scope('accuracy') as scope:
            correct = tf.equal(tf.argmax(prediction,1),tf.argmax(label,1))
            correct = tf.cast(correct, tf.float16)
            accuracy = tf.reduce_mean(correct)
            tf.summary.scalar(scope.name+'/accuracy', accuracy)
    return accuracy

def learning_rate(parameters, global_step):
    learning_rate_base = parameters[0]
    learning_rate_step = parameters[1]
    learning_rate_decay = parameters[2]

    return tf.train.exponential_decay(learning_rate_base, global_step, learning_rate_step, learning_rate_decay, staircase=False, name = 'learning_rate')