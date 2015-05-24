__author__ = 'aditya'

from matplotlib.mlab import PCA
import numpy as np


#1.) Read text file
f = open('/Users/aditya/Downloads/UCI HAR Dataset/train/subject_train.txt', "r")
n_subjects = f.read().split()
f = open('/Users/aditya/Downloads/UCI HAR Dataset/train/X_train.txt', "r")
n_train_feature = f.read().split()

A = np.array(n_train_feature)
t_matrix = np.reshape(A, (-1, 561))
t_pca  = PCA(t_matrix)


f = open('/Users/aditya/Downloads/UCI HAR Dataset/train/y_train.txt', "r")
n_train_label = f.read().split()


