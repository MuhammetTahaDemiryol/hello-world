# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:16:33 2022

@author: Taha
"""

import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

  
def getParameters():
    l = int(input('Enter length of the cube: '))
    ss = int(input('Enter step size: '))
    return l,ss


def  generatePointCloud(l):
    return np.random.randint(0,l,size=(200,3))


def writePCToDataFrameAndFile(array):
    s1=pd.Series(data=pc[:,0])
    s2=pd.Series(data=pc[:,1])
    s3=pd.Series(data=pc[:,2])
    
    df=pd.DataFrame({"axis_1":s1,"axis_2":s2,"axis_3":s3})
    
    df.to_csv('test.csv',index=None,sep='/')
    
    return df


def findPointsInAVoxel(pc,l,ss):
    
    
    for i in range (0,l,ss):
        for j in range (0,l,ss):
            for k in range (0,l,ss):
               voxels[(i,j,k)]=pc[((pc[:,0]>=i) & (pc[:,0]<i+ss)) & \
                                  ((pc[:,1]>=j) & (pc[:,1]<j+ss)) & \
                                  ((pc[:,2]>=k) & (pc[:,2]<k+ss))] 
    return voxels    


def calculateVoxelMeans(voxels,l,ss):
    means=np.zeros((len(voxels.keys()),3))
    index=0
    for key,value in voxels.items():
        means[index]=np.mean(value,axis=0)
        index += 1
    np.savetxt('vovel_means.csv', means, delimiter= ",")
    

def plotFilteredPoints(test,):
    cloud=pd.read_csv(test.csv)    
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d')

voxels={}

l,ss = getParameters()
pc = generatePointCloud(l)
df=writePCToDataFrameAndFile(pc)
voxels=findPointsInAVoxel(pc,l,ss)
calculateVoxelMeans(voxels,l,ss)  



        

