import tensorflow as tf
import tensorflow.contrib.slim as slim


def conv_bn_relu6(net, output_channel, kernel, stride, use_bias, phase_train, scope):
    batch_norm_params = {
        'is_training': phase_train,
        'zero_debias_moving_mean': True,
        # Decay for the moving averages.
        'decay': 0.995,
        # epsilon to prevent 0s in variance.
        'epsilon': 0.001,
        # force in-place updates of mean and variance estimates
        'updates_collections': None,
        # Moving averages ends up in the trainable variables collection
        'variables_collections': [tf.GraphKeys.TRAINABLE_VARIABLES],
    }
    if use_bias == 0:
        conv = slim.conv2d(net, output_channel, kernel, stride=stride, normalizer_fn=slim.batch_norm,
                           normalizer_params=batch_norm_params, activation_fn=tf.nn.relu6, biases_initializer=None, scope=scope)
    else:
        conv = slim.conv2d(net, output_channel, kernel, stride = stride, normalizer_fn=slim.batch_norm,
                           normalizer_params=batch_norm_params,  activation_fn=tf.nn.relu6, scope=scope)
    return conv


def bottleneck(input, t, c, n, s, phase_train, index):
    net = input
    batch_norm_params = {
        'is_training': phase_train,
        'zero_debias_moving_mean': True,
        # Decay for the moving averages.
        'decay': 0.995,
        # epsilon to prevent 0s in variance.
        'epsilon': 0.001,
        # force in-place updates of mean and variance estimates
        'updates_collections': None,
        # Moving averages ends up in the trainable variables collection
        'variables_collections': [tf.GraphKeys.TRAINABLE_VARIABLES],
    }
    with slim.arg_scope([slim.conv2d, slim.separable_conv2d],
                        weights_initializer=slim.initializers.xavier_initializer(),
                        normalizer_fn=slim.batch_norm,
                        normalizer_params=batch_norm_params,
                        activation_fn=tf.nn.relu6,
                        reuse=None):
        for i in range(n):
            with tf.variable_scope('bneck%d' % index) as scope:
                if s != 1 and i != 0:
                    s = 1
                input_channel = net.shape[-1]
                if input_channel == c:
                    input_net = net
                if t != 1:
                    output_channel = t*input_channel
                    index1 = 2
                    net = slim.conv2d(net, output_channel, [
                                      1, 1], scope='bneck%d_conv%d_1' % (index, i+1))
                else:
                    index1 = 1
                net = slim.separable_conv2d(net, None, [
                                            3, 3], 1, s, padding='SAME',  scope='bneck%d_depthwise1_%d' % (index, i+1))
                net = slim.conv2d(net, c, [
                                  1, 1], stride=1, activation_fn=None, scope='bneck%d_conv%d_%d' % (index, i+1, index1))
                if input_channel == c and s == 1:
                    net = input_net + net
    return net


def inference(input, model_def, phase_train):
    net = input
    (index_conv, index_bneck, index_pool) = (1, 1, 1)
    for (t, c, n, n1, s) in model_def:
        if t == 0 or t == -1:
            layer = 'conv' + str(index_conv)
            index_conv += 1
            net = conv_bn_relu6(net, c, [n, n1], s, t, phase_train, layer)
        elif t == 1 and c == 1:
            layer = 'pool' + str(index_pool)
            index_pool += 1
            net = slim.avg_pool2d(
                net, [n,n1], stride=s,padding='SAME', scope=layer)
        elif t == -2:
            pass
        else:
            net = bottleneck(net, t, c, n, s, phase_train, index_bneck)
            index_bneck += 1
    net = tf.reshape(net, [net.shape[0], net.shape[-1]], name='logits')
    return net
