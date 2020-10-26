# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:24:05 2020

@author: Anna
"""

### Rolling window creation

import pandas as pd
import glob

inputfilepathweeks = r'D:\Data\cleaned data\from server\one week window\*.xlsx'
df = pd.read_excel(r'D:/Data/cleaned data/from server/one week window/starting file/0601_0604_pagecommentsmerged.xlsx')


count=0
window_list=[]
for file in glob.iglob(inputfilepathweeks):
    count=count+1
    dfnew = pd.read_excel(file)
    dfcombined = pd.concat([df,dfnew])
    window_list.append(dfcombined)
    df = dfnew
    print(count)
    

window1=window_list[0]

