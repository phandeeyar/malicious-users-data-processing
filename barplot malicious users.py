# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:40:04 2020

@author: Anna
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#######################
fig, ax = plt.subplots(figsize=(5,8.5))
plt.subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.1)

matplotlib.rc('font', family='Arial')

plt.rc('axes', titlesize=20)

plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10) 

users = malicious_users['user_id'][:30]
user_series = pd.Series()
for user in users:
    result = ''.join([i for i in user if not i.isdigit()])
    result = result.rstrip()
    result = pd.Series(result)
    print(result)
    user_series = user_series.append(result)


y_pos = np.arange(len(user_series))
malicious_score = malicious_users['malicious_score'][:30]
ax.barh(y_pos, malicious_score, align='center', height=0.8)
ax.set_yticks(y_pos)
ax.set_yticklabels(user_series)
ax.invert_yaxis()
ax.set_xlabel('Malicious score', fontsize=14, labelpad=12)
ax.set_title('Malicious users identified', pad=15)

plt.show()


#plt.close()






