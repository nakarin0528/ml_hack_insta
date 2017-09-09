from RGB2Lab import rgb2lab
from kmeanscolor import colcheck
from PIL import Image
import numpy as np
from LabDis import labdis

IMSIZE = 50

def aveLab(targetimg,k): #画像パスと代表色数
    result = colcheck(targetimg,k)

    Labs = []

    for rgb in result:
        Labs.append(rgb2lab(rgb))
    
    sum = 0.0
    counter = 0.0

    if not k == 2:
        for i in range(k):
            if i == k-1:
                break;
            for s in range(i+1,k-1):
                sum += labdis(Labs[i],Labs[s])
                counter += 1.0

    re = sum/counter

    return(re)

def aveLab2(targetimg,k):
    result = colcheck(targetimg,k)
    Labs = []
    for rgb in result:
        Labs.append(rgb2lab(rgb))
    return(Labs)

if __name__ == '__main__':
    aveLab("img/all/col.jpg",4)
    aveLab("img/all/mono.jpg",4)
