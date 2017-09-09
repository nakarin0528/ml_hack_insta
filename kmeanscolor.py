import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import collections

def colcheck(path,k):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    flatten = img.reshape(-1,3)
    pred = KMeans(n_clusters=k).fit(flatten)
    out = zip(pred.labels_, flatten)

    return pred.cluster_centers_
if __name__ == '__main__':
    re = colcheck("img/all/0.jpg",2)
    print(re)
