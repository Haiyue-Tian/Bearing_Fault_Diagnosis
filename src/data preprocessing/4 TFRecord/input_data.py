import numpy as np
import os

def mat2py(path, classes) :
        l_Normal = 0
        l_Inner_Race = 1
        l_Outer_Race = 2
        l_Ball = 3
        Normal = []
        label_Normal = []
        Inner_Race = []
        label_Inner_Race = []
        Outer_Race = []
        label_Outer_Race = []
        Ball = []
        label_Ball = []
        

        for name in classes:
                file_name = os.listdir(path + name)
                length = len(file_name)
                for i in range(length) :
                        matpath = path + name + '/' + file_name[i]
                        exec("%s.append(matpath)"%name)
                        exec("label_%s.append(l_%s)"%(name,name))              
                        

        # merge images and labels
        image_list = np.hstack((locals()[classes[0]], locals()[classes[1]], locals()[classes[2]], locals()[classes[3]] ))
        label1 = 'label_' + classes[0]
        label2 = 'label_' + classes[1]
        label3 = 'label_' + classes[2]
        label4 = 'label_' + classes[3]
        label_list = np.hstack((locals()[label1],locals()[label2],locals()[label3],locals()[label4]))

        # shuffle images and lists
        temp = np.array([image_list, label_list])
        temp = temp.transpose()
        np.random.shuffle(temp)

        # transfer images and labels to list
        all_image_list = list(temp[:,0])
        all_label_list = list(temp[:,1])
        all_label_list = [int(float(i)) for i in all_label_list]
        label = np.array(all_label_list)
        image = np.array(all_image_list)
        return image, label
