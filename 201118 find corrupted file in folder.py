# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:57:54 2020

@author: Anna
"""

inputfilepath = r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Data\from server\20200908_20201001\*.xlsx'

import pandas as pd
import glob

count=0
for filepath in glob.iglob(inputfilepath):
    count=count+1
    print(count)
    dfnew = pd.read_excel(filepath)