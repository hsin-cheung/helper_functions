#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


class DataProcessing(object):
    
    def __init__(self, xVals, yVals):
        
        '''
        xVals, yVals should be 1d numpy array with the same lenth
        '''
        
        self.xVals = xVals
        self.yVals = yVals
    
    def get_xVals(self):
        return self.xVals
    
    def get_yVals(self):
        return self.yVals
    
    def devide_by_max(self): #Normalize by max y value
        '''
        return xVals and normalized yVals
        '''
        return self.get_xVals(), self.get_yVals()/max(self.get_yVals())
    
    def devide_by_specific(self, xValue): #Normalize by a specific y value of x point
        yValue = self.get_yVals()[np.where(self.get_xVals()==xValue)[0][0]]
        return self.get_xVals(), self.get_yVals()/yValue

    def integrate(self, start, end): #Set the integration range, start and end not necessary to be valid points in the data
        '''
        the integration does not include the end point
        '''
        idx_1, idx_2 = np.where(self.get_xVals()>=start)[0][0], np.where(self.get_xVals()<=end)[0][-1]
        x_range = self.get_xVals()[idx_1:idx_2+1]
        y_range = self.get_yVals()[idx_1:idx_2+1]
        return np.trapz(y_range, x_range)
        

    
    

