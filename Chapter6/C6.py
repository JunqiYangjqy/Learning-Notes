# -*- coding: utf-8 -*-
"""
@author: Jarry
"""
#Chapter 6 - Data Load, Storage, and File Format

import pandas as pd
import numpy as np

df=pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples/ex1.csv')
#or
#df=pd.read_table('Datasets/examples/ex1.csv',sep=',')

#Sometimes the file doesn't contain the header
#df2=pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples\ex2.csv')
#Automatically assign the header: header=None
df2=pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples\ex2.csv',header=None)
#Assign the header by us
df2=pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples\ex2.csv',names=['a','b','c','d','message'])

#Also, we can specify the index column with index_col
headers=['a','b','c','d','message']
df2=pd.read_csv('D:\GitHub\Repos\Learning-Notes\Datasets\examples\ex2.csv',names=headers,index_col='message')


