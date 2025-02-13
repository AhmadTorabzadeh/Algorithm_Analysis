#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:03:39 2024

@author: ahmadtorabzadeh
"""

def solve():
    
    n, k, city_populations=read_input() 
    A=merge_sort(city_populations) 
    target=A[k-1]
    return target



def merge(B,C):
    A=[]
    n1=len(B)
    n2=len(C)
    i=0
    j=0
    
    while i<n1 or j<n2:
        if j>=n2 or (i<n1 and B[i][1]<=C[j][1]):
            
            A.append(B[i])
            i+=1
        elif j<n2:
            
            A.append(C[j])
            j+=1
    return A   


def merge_sort(A):
     
    if len(A)==1:
        return A
    else:
        x=len(A)//2
        B=merge_sort(A[:x])
        C=merge_sort(A[(x):])
        A=merge(B, C)
    return A



def read_input():
    n, k = map(int, input().split())
    city_populations = []
    for _ in range(n):
        idx, population = map(int, input().split())
        city_populations.append((idx, population))
    return n, k, city_populations



target=solve()
print(target[0],target[1])
