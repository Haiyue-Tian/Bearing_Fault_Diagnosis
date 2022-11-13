import argparse
import numpy as np

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    ### Train
    parser.add_argument('--train_log_dir', type=str, metavar='', help='Directory where to write event logs.',
        default='../../data/logs')
    parser.add_argument('--train_model_dir', type=str, metavar='', help='Directory where to write models',
        default='../../data/logs')
    parser.add_argument('--model', type=str, metavar='', help='Model definition',
        default='models.model2_1')
    parser.add_argument('--TFRecord_dir', type=str, metavar='', help='Directory where to load tfrecords',
        default='../../data/TFRecorder/Train.tfrecords')
    parser.add_argument('--n_epochs', type=int, metavar='', help='The number of epoch',
        default=None)
    parser.add_argument('--batch_size', type=int, metavar='', help='The size of each batch',
        default=128)
    parser.add_argument('--min_after_dequeue', type=int, metavar='', help='min_after_dequeue',
        default=10)
    parser.add_argument('--n_classes', type=int, metavar='', help='The number of classes',
        default=4)
    parser.add_argument('--phase_train', type=bool, metavar='', help='Training or not',
        default=True)
    parser.add_argument('--optimizer', type=str, metavar='', help='The method of training',
        default='ADAM')
    parser.add_argument('--max_step', type=int, metavar='', help='The max step of training',
        default=20000)
    parser.add_argument('--name_ckpt', type=str, metavar='', help='The name of ckpt',
        default='model.ckpt')
    parser.add_argument('--learning_rate_parameters', type=np.array, metavar='', help='[learning_rate_base, learing_rate_step, learning_rate_decay]',
        default=[0.1, 50, 0.9])
    parser.add_argument('--model_def', type=np.array, metavar='', help='The structure of bottleneck, [t, c, n, s]',
        default= [[0, 16, 3, 3, 2],
                  [1, 16, 1, 0, 2], # [conv2d=0 without bias/ conv2d=-1 with bias, output_channel, kernel_size0, kernel_size1, stride]
                  [6, 32, 2, 0, 2], # [t, c, n, _, s]
                  [6, 64, 3, 0, 2],# [full_connection=-2, with bias=0/without bias=1, output, _, _ ]
                  [0, 1280, 1, 1, 1],
                  [1, 1, 2, 2, 2],
                  [0, 4, 1,1, 1]])


    ###  Test
    parser.add_argument('--Test_TFRecord_dir', type=str, metavar='', help='Directory where to load tfrecords',
        default='../../data/TFRecorder/Test.tfrecords')
    parser.add_argument('--test_phase_train', type=bool, metavar='', help='Training or not',
        default=False)
    parser.add_argument('--test_n_epochs', type=int, metavar='', help='The number of epoch for test',
        default=1)

    ### calculate the amount of calculation and memory
    parser.add_argument('--input', type=np.array, metavar='', help='The size of input',
        default=[32, 32, 1])
    parser.add_argument('--model_structure', type=np.array, metavar='', help='The structure of bottleneck, [t, c, n, s]',
        default= [[0, 32, 3, 3, 1], # [conv2d=0 without bias/ conv2d=-1 with bias, output_channel, kernel_size0, kernel_size1, stride]
                  [1, 16, 1, 0, 1], # [t, c, n, _, s]
                  [6, 24, 2, 0, 2],# [full_connection=-2, with bias=0/without bias=1, output, _, _ ]
                  [6, 32, 3, 0, 2],
                  [6, 64, 4, 0, 2],
                  [6, 96, 3, 0, 1],
                  [6, 160, 3, 0, 2],
                  [6, 320, 1, 0, 1],
                  [0,1280, 1, 1, 1],
                  [1, 1, 2, 2, 2], # [pooling_flag=1, pooling_flag=1, kernel_size, kernel_size, stride]
                  [0, 4, 1, 1, 1]])
    return parser.parse_args(argv)

