#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random
import plotly.express as px
import pandas as pd

def InsertionSort(Array):
    for i in  range(1, len(Array)):
        key_value=Array[i]
        j=i-1
        while j>=0 and key_value<Array[j]:
            Array[j+1]=Array[j]
            j=j-1
        Array[j+1]=key_value
        
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




insertion_times = []
merge_times = []

Array_sizes = list(range(10, 3000, 100))

for size in Array_sizes:

    data = [random.randint(1, 100) for _ in range(size)]

    start_time = time.time()
    InsertionSort(data.copy())
    insertion_times.append(time.time() - start_time)

    start_time = time.time()
    MergeSort(data.copy())
    merge_times.append(time.time() - start_time)


df = pd.DataFrame({'Array Size': Array_sizes,
                   'Insertion Time': insertion_times,
                   'Merge Time': merge_times})


fig = px.line(df, x='Array Size', y=['Insertion Time', 'Merge Time'],
              labels={'value': 'Run Time', 'variable': 'Sort Algorithm'},
              title='Run Time vs Sample Data Size')

fig.show()

