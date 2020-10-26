# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:07:55 2020

@author: Anna
"""

import pandas as pd
import numpy as np

##################################### 
hs_freq20largest_count = np.array([])
hs_freq20largest_count_df = pd.DataFrame()

for df in hs_frequency20largest_list:
    hsf20largest = df['user_id'] #series
    hs_freq20largest_count = np.append(hs_freq20largest_count, [hsf20largest])
    
hs_freq20largest_count_df['user_id'] = hs_freq20largest_count
hs_freq20largest_count_score = hs_freq20largest_count_df['user_id'].value_counts()
hs_freq20largest_count_score = hs_freq20largest_count_score.reset_index()
hs_freq20largest_count_score.rename(columns={'index':'user_id', 'user_id':'hs_freq'}, inplace=True)

del hsf20largest
del hs_freq20largest_count
del hs_freq20largest_count_df


#####################################
postfreq20largest_count = np.array([])
postfreq20largest_count_df = pd.DataFrame([])

for df in postfreq20largest_list:
    pf20largest = df['user_id']
    postfreq20largest_count = np.append(postfreq20largest_count, [pf20largest])

postfreq20largest_count_df['user_id'] = postfreq20largest_count
postfreq20largest_count_score = postfreq20largest_count_df['user_id'].value_counts()
postfreq20largest_count_score = postfreq20largest_count_score.reset_index()
postfreq20largest_count_score.rename(columns={'index':'user_id', 'user_id':'postfreq'}, inplace=True)

del pf20largest
del postfreq20largest_count
del postfreq20largest_count_df


#####################################
hsratio20largest_count = np.array([])
hsratio20largest_count_df = pd.DataFrame([])

for df in hsratio20largest_list:
    hsr20largest = df['user_id']
    hsratio20largest_count = np.append(hsratio20largest_count, [hsr20largest])
    
hsratio20largest_count_df['user_id'] = hsratio20largest_count
hsratio20largest_count_score = hsratio20largest_count_df['user_id'].value_counts()
hsratio20largest_count_score = hsratio20largest_count_score.reset_index()
hsratio20largest_count_score.rename(columns={'index':'user_id', 'user_id':'hsratio'}, inplace=True)

del hsr20largest
del hsratio20largest_count
del hsratio20largest_count_df


#####################################
av_overperforming20largest_count = np.array([])
av_overperforming20largest_count_df = pd.DataFrame([])

for df in av_overperforming20largest_list:
    aop20largest = df['user_id']
    av_overperforming20largest_count = np.append(av_overperforming20largest_count, [aop20largest])

av_overperforming20largest_count_df['user_id'] = av_overperforming20largest_count
av_overperforming20largest_count_score = av_overperforming20largest_count_df['user_id'].value_counts()
av_overperforming20largest_count_score = av_overperforming20largest_count_score.reset_index()
av_overperforming20largest_count_score.rename(columns={'index':'user_id', 'user_id':'av_overperforming'}, inplace=True)

del aop20largest
del av_overperforming20largest_count
del av_overperforming20largest_count_df


#####################################
degreecentrality20largest_count = np.array([])
degreecentrality20largest_count_df = pd.DataFrame([])

for df in degreecentrality20largest_list:
    df = df.reset_index()
    df.rename(columns={'index':'user_id'}, inplace=True)
    dc20largest = df['user_id']
    degreecentrality20largest_count = np.append(degreecentrality20largest_count, [dc20largest])
    
degreecentrality20largest_count_df['user_id'] = degreecentrality20largest_count
degreecentrality20largest_count_score = degreecentrality20largest_count_df['user_id'].value_counts()
degreecentrality20largest_count_score = degreecentrality20largest_count_score.reset_index()
degreecentrality20largest_count_score.rename(columns={'index':'user_id', 'user_id':'degree_centrality'}, inplace=True)

del dc20largest
del degreecentrality20largest_count
del degreecentrality20largest_count_df


######################################
betweenness20largest_count = np.array([])
betweenness20largest_count_df = pd.DataFrame([])

for df in betweenness20largest_list:
    df = df.reset_index()
    df.rename(columns={'index':'user_id'}, inplace=True)
    bt20largest = df['user_id']
    betweenness20largest_count = np.append(betweenness20largest_count, [bt20largest])
    
betweenness20largest_count_df['user_id'] = betweenness20largest_count
betweenness20largest_count_score = betweenness20largest_count_df['user_id'].value_counts()
betweenness20largest_count_score = betweenness20largest_count_score.reset_index()
betweenness20largest_count_score.rename(columns={'index':'user_id', 'user_id':'betweenness_centrality'}, inplace=True)

del bt20largest
del betweenness20largest_count
del betweenness20largest_count_df


######################################
eigenvector20largest_count = np.array([])
eigenvector20largest_count_df = pd.DataFrame([])

for df in eigenvector20largest_list:
    df = df.reset_index()
    df.rename(columns={'index':'user_id'}, inplace=True)
    ei20largest = df['user_id']
    eigenvector20largest_count = np.append(eigenvector20largest_count, [ei20largest])

eigenvector20largest_count_df['user_id'] = eigenvector20largest_count
eigenvector20largest_count_score = eigenvector20largest_count_df['user_id'].value_counts()
eigenvector20largest_count_score = eigenvector20largest_count_score.reset_index()
eigenvector20largest_count_score.rename(columns={'index':'user_id','user_id':'eigenvector_centrality'}, inplace=True)

del ei20largest
del eigenvector20largest_count 
del eigenvector20largest_count_df


#######################################
pagerank20largest_count = np.array([])
pagerank20largest_count_df = pd.DataFrame([])

for df in pagerank20largest_list:
    df = df.reset_index()
    df.rename(columns={'index':'user_id'}, inplace=True)
    pr20largest = df['user_id']
    pagerank20largest_count = np.append(pagerank20largest_count, [pr20largest])
    
pagerank20largest_count_df['user_id'] = pagerank20largest_count
pagerank20largest_count_score = pagerank20largest_count_df['user_id'].value_counts()
pagerank20largest_count_score = pagerank20largest_count_score.reset_index()
pagerank20largest_count_score.rename(columns = {'index':'user_id', 'user_id':'pagerank'}, inplace=True)

del pr20largest
del pagerank20largest_count
del pagerank20largest_count_df


#######################################
malicious_users = pd.merge(hs_freq20largest_count_score, postfreq20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, hsratio20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, av_overperforming20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, degreecentrality20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, betweenness20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, eigenvector20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, pagerank20largest_count_score, how='outer', on='user_id')

malicious_users = malicious_users.fillna(0)


malicious_users['malicious_score'] = (malicious_users['hs_freq']/(malicious_users['hs_freq']+0.00001))*(malicious_users['hs_freq']+malicious_users['postfreq']+malicious_users['hsratio']+malicious_users['degree_centrality']+malicious_users['pagerank'])
malicious_users = malicious_users.sort_values(by=['malicious_score'], ascending=False)
malicious_users = malicious_users.round()

malicious_users.to_excel(r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Analysis\Malicious users\200921results.xlsx')