# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 02:33:03 2022

@author: Taha
"""

import random

def main():
    p1 = []
    p2 = []
    p1 = initalizeFeatures(p1,1)
    print("Features for P1",p1)
    p2 = initalizeFeatures(p2,2)
    print("Features for P2",p2)
    print("\nMaximum feature of p1 is :",max(p1))
    print("Maximum feature of p2 is :",max(p2))
    min_feature_p1 = normalize(p1,max(p1))
    min_feature_p2 = normalize(p2,max(p2))
    print("\nMinimum of normalized minimum feature is:", min(min_feature_p1,min_feature_p2))
    
def initalizeFeatures(point,id_):
    for i in range(3):
        if id_ == 1:
            point.append(random.randint(7, 15))
        else:
            point.append(random.randint(6, 13))
    return point
def normalize(point,max_feature):
    norm_list = []
    for i in range(len(point)):
        norm_list.append(point[i]/max_feature)
    print("\nNormalized Features")
    print(norm_list)
    return min(norm_list)
main()