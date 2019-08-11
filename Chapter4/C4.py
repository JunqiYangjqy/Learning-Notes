# -*- coding: utf-8 -*-
"""
@author: Jarry
"""

#Chapter 4 - NumPy

import numpy as np

data = np.random.randn(2,3) #generate an array with random numbers

data * 10 #math operations can be directly used

data.shape
data.dtype

#Generate array with array function
data1=[6,7.5,8,8.5,0,1]
arr1=np.array(data1)
arr1

data2=[[1,2,3,4],[5,6,7,8]] #A list that has a list
arr2=np.array(data2)
arr2 #two-dimensional array
type(arr2)

arr2.ndim #Check the dimension
arr2.shape

#To create an array with all 0
np.zeros(5)
np.zeros((2,2))
#To create multi-dimenson array, need to send a tuple value

np.arange(10) #the NumPy version of Python range()

arr=np.array([1,2,3,4,5])
arr.dtype
float_arr=arr.astype(np.float64) #Use astype() to change the data type
float_arr.dtype
#If we transform a float array to int, the value after radix point will be discarded
arr=np.array([1.1,2.2,3.3,4.4,5.5])
arr.dtype
arr.astype(np.int32)

#NumPy Array Mathematics
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
arr
arr*arr
arr-arr
#It will automatically apply the operation for each items without any for loop

#The comparison between same size array will generate a bool array
arr2=np.array([[0,4,1],[7,2,12]])
arr2>arr




