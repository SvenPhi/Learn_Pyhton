# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:09:14 2018

@author: Sven

This file creates the data for predicting the sex.
"""
def create_data():
    from pandas import DataFrame

    column_names = ['height', 'weight', 'shoe_size', 'sex']
    
    
    data = [[181, 80, 44, 'male'], [177, 74, 43, 'female'], [160, 60, 38, 'female'],
            [154, 54, 37, 'female'], [166, 65, 40, 'male'], [190, 90, 47, 'male'],
            [175, 64, 39, 'male'], [177, 70, 40, 'female'], [159, 55, 37, 'male'],
            [171, 75, 42, 'female'], [181, 85, 43, 'male']]

    return DataFrame(data, columns = column_names)

