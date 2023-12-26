#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def LoadData(filename, skiprows=0, max_rows=0, delimiter = None, 
             col_x = None, col_y = None):
    '''
    read data from the file, return numpy arrays of xVals and yVals
    filename: a string represent the file
    skiprows: int, skip the first skiprows lines
    max_rows: int, read max_rows rows of content after skiprows lines
    delimiter: delimiter that separates columns
    col_x: column number of xVals in the original file, start from 0
    col_y: column number of yVals in the original file, start from 0
    '''
    file = np.loadtxt(filename, skiprows=skiprows, max_rows=max_rows, delimiter = delimiter, usecols=(col_x, col_y))
    xVals = file[:, 0]
    yVals = file[:, 1]
    return xVals, yVals





