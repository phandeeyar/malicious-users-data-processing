# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:47:09 2020

@author: Anna
"""

#Wordcloud    

window = window_list[0] #change this to the window data
hs_expression_freq = window['hate_speech_item1'].value_counts()
hs_expression_freq = hs_expression_freq.reset_index()



target_count = target_count.reset_index()
hs_expression_freq.rename(columns={'index':'word', 'hate_speech_item1':'count'}, inplace=True)
bag = hs_expression_freq

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 


#hs_expression_freq_dict = hs_expression_freq.to_dict()

matplotlib.rc('font', family='Pyidaungsu-2.5_regular') #this doesn't work

#PYIDAUNGSU-2.5_REGULAR
d = {}
for a, x in bag.values:
    d[a] = x

#import matplotlib.pyplot as plt
from wordcloud import WordCloud

wordcloud = WordCloud()
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
