#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Author: Ashish Shah
# Date: 20/09/2023

# CSE-5311 Assignment 


import time
import random
import plotly.express as px
import pandas as pd

def Heapify(Arr, n, i):
    greatest = i 
    left = 2*i+1
    right = 2*i+2
    
    if left<n and Arr[i]<Arr[left]:
        greatest=left
        
    if right<n and Arr[greatest]<Arr[right]:
        greatest=right
        
        
    if greatest!=i:
        (Arr[i], Arr[greatest])=(Arr[greatest], Arr[i])
        Heapify(Arr, n, greatest)

def HeapSort(Array):
    n=len(Array)
    
    for i in range(n//2 - 1, -1, -1):
        Heapify(Array, n, i)
    
    for i in range(n-1,0,-1):
        (Array[i], Array[0])=(Array[0], Array[i])
        Heapify(Array, i, 0)
    
    
    
    
        
def MergeSort(Array):
    if len(Array)>1:
        
        mid=len(Array)//2
        left=Array[:mid]
        right=Array[mid:]
        
        MergeSort(left)
        MergeSort(right)
        
        i=j=k=0
        
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                Array[k]=left[i]
                i+=1
            else:
                Array[k]=right[j]
                j+=1
                
            k+=1
            
        while i < len(left):
            Array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            Array[k] = right[j]
            j += 1
            k += 1



# Driver Code: 

Heapsort_times = []
Mergesort_times = []

Array_sizes = list(range(10, 3000, 50))

for size in Array_sizes:
    
    heapS_time=0
    mergeS_time=0
    x=20
    
    for i in range(x):
        
        data = [random.randint(1, 100) for _ in range(size)]
        
        start_time = time.time()
        HeapSort(data.copy())
        heapS_time+=time.time() - start_time
        
        start_time = time.time()
        MergeSort(data.copy())
        mergeS_time+=time.time() - start_time
    
    avg_heap_time= heapS_time/x
    avg_merge_time = mergeS_time/x
    
    Heapsort_times.append(avg_heap_time)
    Mergesort_times.append(avg_merge_time)


df = pd.DataFrame({'Array Size': Array_sizes,
                   'Heapsort Time': Heapsort_times,
                   'Mergesort Time': Mergesort_times})


fig = px.line(df, x='Array Size', y=['Heapsort Time', 'Mergesort Time'],
              labels={'value': 'Run Time', 'variable': 'Sort Algorithm'},
              title='Run Time vs Sample Data Size')

fig.show()

