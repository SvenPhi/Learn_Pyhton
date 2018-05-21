# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:57:51 2018

@author: Sven

Simple decisiopn tree classifier example for learning python.
"""
from sklearn import calibration
import sex_data as sd

data = sd.create_data()

clf = calibration.CalibratedClassifierCV()
clf = clf.fit(data.loc[:,['height','weight','shoe_size']], data.loc[:,'sex'])

prediction = clf.predict([[190, 70, 43]])
print(prediction)