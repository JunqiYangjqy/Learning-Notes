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

#NumPy index and slice
arr=np.arange(10)

arr[5]
arr[5:9]
arr[:8]

#assign the value - one for all
arr[5:8]=10
arr #array([ 0,  1,  2,  3,  4, 10, 10, 10,  8,  9])
#Notice: the slice is not a new array, it's the view of the original array
#any changes of the slice will be reflected in the original array
arrslice=arr[5:8]
arrslice[0]=68 #array([68, 12, 12])
arrslice
arr #array([ 0,  1,  2,  3,  4, 68, 12, 12,  8,  9])

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]
arr2d[2][0]

#Bool Index
names=np.array(['Bob','Joe','Will','Bob','Will','Jow','Joe'])
data=np.random.randint(0,100,(7,4)) #(7,4) is the size of the array,0 is the low while 100 is the high

names=='Bob' # this will generate a bool array
# array([ True, False, False,  True, False, False, False])

#When indexing array we can pass bool array
data[names=='Bob']
#array([[32, 90, 93, 67],
#      [15, 28, 54, 74]])

data[names=='Bob',2:] #Indexing the columns

#Python keywords 'and' and 'or' is not working for bool array, using & and | 

#Magical Index
arr=np.empty((8,4))

for i in range(8):
    arr[i]=i

arr

#To choose a subset that has an order, we can pass a list or array with this order
#e.g.
arr[[1,2,3,4]]
"""
The result is 
array([[1., 1., 1., 1.],
       [2., 2., 2., 2.],
       [3., 3., 3., 3.],
       [4., 4., 4., 4.]])

if the index is negative, it will choose reversely
e.g. arr[[-3,-2,-1]]
The result is 
array([[5., 5., 5., 5.],
       [6., 6., 6., 6.],
       [7., 7., 7., 7.]])
"""

#Transpose

arr=np.arange(15).reshape((3,5))

arr
arr.T
np.dot(arr.T,arr)

#General Functions
#sqrt() or exp()
data=[1,4,9,16,25,36,49,64]
arr=np.array(data)

np.sqrt(arr)

np.exp(arr)

x=np.random.randn(8)
y=np.random.randn(8)
np.maximum(x,y)

arr=np.random.randn(8)
remainder, whole_part = np.modf(arr)
remainder
whole_part

#Vectorization
#Use simple array expression to replace the complex for loops
#E.g. calculate sqrt(x^2 + y^2) for mesh numbers
#Use np.meshgrid to receive two single-dimenson array
points=np.arange(-5,5,0.1)
xs,ys = np.meshgrid(points,points)

z = np.sqrt(xs**2 + ys **2)

import matplotlib.pyplot as plt
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
plt.title("Image plot for $\sqrt{x^2+y^2}$ for a grid of values")
plt.show()

#Page111






