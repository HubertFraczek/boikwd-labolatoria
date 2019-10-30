#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:56:20 2019
 
@author: chris
"""
 
import numpy as np
 
A=np.array([[1,2/3,2,5/2,5/3,5],[3/2,1,3,10/3,3,9],[1/2,1/3,1,4/3,7/8,5/2],[2/5,3/10,3/4,1,5/6,12/5],[3/5,1/3,8/7,6/5,1,3],[1/5,1/9,2/5,5/12,1/3,1]])
 
B=np.array([[1,2/5,3,7/3,1/2,1,2],[5/2,1,4/7,1,1,3,2/3],[1/3,7/4,1,1/2,2,1/2,1],[3/7,1,2,1,4,2,6],[2,1,1/2,1/4,1,1/2,3/4],[1,1/3,2,1/2,2,1,5/8],[1/2,3/2,1,1/6,4/3,8/5,1]])
 
C=np.array([[1,2/3,2/15,1,8,12/5,1,1/2],[3/2,1,1,2,1,2/3,1/6,1],[15/2,1,1,5/2,7/8,2,1,1/5],[1,1/2,2/5,1,4/3,1,2/7,1],[1/8,1,8/7,3/4,1,1/5,2/7,1],[5/12,3/2,1/2,1,5,1,3,2],[1,6,1,7/2,7/2,1/3,1,3/11],[2,1,5,1,1,1/2,11/3,1]])
 
D=[[0,1,1,-1,-1,1,-1],[-1,0,0,1,1,-1,0],[-1,0,0,0,1,1,-1],[1,-1,0,0,1,0,1],[1,0,-1,-1,0,1,-1],[-1,1,-1,1,-1,0,0],[1,0,1,-1,1,0,0]]
 
E=[[0,1,0,0,-1],[-1,0,0,0,1],[0,0,0,1,0],[0,0,-1,0,0],[1,-1,0,0,0]]
 
F=[[0,-1,1,-1,1,-1,1,-1,1],[1,0,1,1,1,-1,-1,-1,-1],[-1,-1,0,-1,1,-1,1,1,1],[1,-1,1,0,-1,1,-1,1,-1],[-1,-1,-1,1,0,-1,1,1,1],[1,1,1,-1,1,0,-1,-1,-1],[-1,1,-1,1,-1,1,0,1,-1],[1,1,-1,-1,-1,1,-1,0,1],[-1,1,-1,1,-1,1,1,-1,0]]
 
def transform(A):
    for i in range (len(A)):
        for j in range (len(A)):
            if (i == j):
                A[i][j] = 0
            elif (A[i][j] > 1):
                A[i][j] = 1
            else:
                A[i][j] = -1
    return A
 
#sprawdz czy macierz turniejowa jest uogolniona
def check(a):
    for i in range (len(A)):
        for j in range (len(A)):
            if (i != j and A[i][j] == 0):
                return False
    return True
 
def isTurniejowa(A):
    for i in range (len(A)):
        for j in range (len(A)):
            if (A[i][j] != -A[j][i]):
                return False
    return True
               
At = transform(A)
Bt = transform(B)
Ct = transform(C)
 
print(check(A))
print(check(B))
print(check(C))
 
print(isTurniejowa(At))
print(isTurniejowa(Bt))
print(isTurniejowa(Ct))
