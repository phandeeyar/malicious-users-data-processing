# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:32:05 2020

@author: Anna
"""
# Needs to be updated but can be used for now

## Groups targeted
import numpy as np
import matplotlib.pyplot as plt

#window = window_list[0]  import window dataset instead of this
window['targeted_group1'].replace({'USDP': 'Party supporters', 'Rohingya/EAOs': 'Ethnic/racial groups', 'Ethical/racial groups':'Ethnic/racial groups','Tatmadaw': 'Military', 'Kachin': 'Ethnic/racial groups', 'Journalist':'Journalist/activist', 'Journalist/activists':'Journalist/activist', 'Muslim':'Ethnic/racial groups', 'NLD':'Party supporters', 'Activist':'Journalist/activist', 'Bamar':'Ethnic/racial groups', 'Migrant workers':'General', 'Tatmadaw/Government': 'Military', 'Chinese':'Ethnic/racial groups', 'Ethnic minority/Migrant workers':'Ethnic/racial groups', 'Commander in Chief':'Military','Prisoner':'General', 'Government':'Military', 'KIA':'Ethnic/racial groups', 'Ethnic minority':'Ethnic/racial groups', 'Rohingya':'Ethnic/racial groups', 'Pro Tatmadaw':'Party supporters', 'AA':'Ethnic/racial groups', 'Rakhine':'Ethnic/racial groups', 'Activist/Journalist':'Journalist/activist', 'Lisu':'Ethnic/racial groups', 'Lawwal':'Ethnic/racial groups', 'Pro Tatmadaw ':'Party supporters', 'Ethnical/racial groups':'Ethnic/racial groups'}, inplace=True)
target_count = window['targeted_group1'].value_counts()

target_count = target_count.reset_index()
target_count.rename(columns={'index':'group', 'targeted_group1':'count'}, inplace=True)

count = target_count['count']
total_count = count.sum()

target_count['percentage'] = target_count['count']/total_count


percentage = target_count['percentage']
groups = target_count['group']
y_pos = np.arange(len(groups))

fig, ax = plt.subplots()
plt.bar(y_pos, percentage)
plt.xticks(y_pos, groups)
#ax.set_xlabel('Groups targeted by hate speech users', fontsize=14, labelpad=12)
ax.set_title('Groups targeted by hate speech users', pad=15)
plt.show()
