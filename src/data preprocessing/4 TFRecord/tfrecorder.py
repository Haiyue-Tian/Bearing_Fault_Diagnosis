import tensorflow as tf  
import numpy as np
import input_data
import scipy.io as sio

def int64_feature(value) :
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
 
def bytes_feature(value):    
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

def floats_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def convert_to_tfrecord(t_path, images, labels):  
        
        filename =  (t_path)  
        n_samples = len(labels)
        if np.shape(images)[0] != n_samples:  
	        raise ValueError('Images size %d does not match label size %d.' %(images.shape[0], n_samples))  

        writer = tf.io.TFRecordWriter(filename)
          
        print('\nTransform start......')
        for i in range(n_samples) :
                try:  
                        dataMat = sio.loadmat(images[i])
                        data = np.array(dataMat['Data'],dtype=np.float32)
                        image_raw = data.flatten()
                        
                        label = int(labels[i])  
                        example = tf.train.Example(features=tf.train.Features(feature={  
                                                        'label':int64_feature(label),  
                                                        'image_raw': floats_feature(image_raw)}))  
                        writer.write(example.SerializeToString())  
                except IOError as e:  
                        print('Could not read:', images[i])  
                        print('error: %s' %e)  
                        print('Skip it!\n')  
        writer.close()  
        print('Transform done!') 

def read_and_decode(filename,  N_CLASSES, n_epochs = None):
    filename_queue = tf.train.string_input_producer([filename], num_epochs = n_epochs )

    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'label': tf.FixedLenFeature([], tf.int64),
                                           'image_raw' : tf.VarLenFeature(tf.float32)})

    img = tf.sparse_tensor_to_dense(features['image_raw'], default_value=0)
    img = tf.reshape(img, [2, 512])
    label = tf.cast(features['label'], tf.int32)
    label = tf.one_hot(label, N_CLASSES, 1, 0)
    return img, label

if __name__ == "__main__" :
        classes = ['Normal','Inner_Race','Outer_Race','Ball']

        mat_path = '../../../data/overlap_sampling_picked_data/train/'
        TFRecorder_path = '../../../data/TFRecorder/Train.tfrecords'
        images, labels = input_data.mat2py(mat_path, classes) 
        convert_to_tfrecord(TFRecorder_path, images, labels)

        mat_path = '../../../data/overlap_sampling_picked_data/test/'
        TFRecorder_path = '../../../data/TFRecorder/Test.tfrecords'
        images, labels = input_data.mat2py(mat_path, classes) 
        convert_to_tfrecord(TFRecorder_path, images, labels)