# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:41:49 2020

@author: Anna
"""
import pandas as pd

w=0 #change this to the window in the dataframe you want to access

hs_freq20largest_count_score = hsusersfreq_list[w]
hs_freq20largest_count_score.rename(columns={'hs_count':'hs_freq'}, inplace=True)
hs_freq20largest_count_score['hs_freq']=1
postfreq20largest_count_score = postfreq20largest_list[w]
postfreq20largest_count_score.rename(columns={'post_count':'postfreq'}, inplace=True)
postfreq20largest_count_score['postfreq']=1
hsratio20largest_count_score = hsratio20largest_list[w]
hsratio20largest_count_score = hsratio20largest_count_score_w1[['user_id','hsratio']]
hsratio20largest_count_score['hsratio']=1
av_overperforming20largest_count_score = av_overperforming20largest_list[w]
av_overperforming20largest_count_score = av_overperforming20largest_count_score_w1[['user_id','av_overperforming']]
av_overperforming20largest_count_score['av_overperforming']=1
degreecentrality20largest_count_score = degreecentrality20largest_list[w]
degreecentrality20largest_count_score = degreecentrality20largest_count_score_w1.reset_index()
degreecentrality20largest_count_score.rename(columns={'index':'user_id'}, inplace=True)
degreecentrality20largest_count_score['degree_centrality']=1
betweenness20largest_count_score = betweenness20largest_list[w]
betweenness20largest_count_score = betweenness20largest_count_score_w1.reset_index()
betweenness20largest_count_score.rename(columns={'index':'user_id'}, inplace=True)
betweenness20largest_count_score['betweenness_centrality']=1
eigenvector20largest_count_score = eigenvector20largest_list[w]
eigenvector20largest_count_score = eigenvector20largest_count_score_w1.reset_index()
eigenvector20largest_count_score.rename(columns={'index':'user_id'}, inplace=True)
eigenvector20largest_count_score['eigenvector_centrality']=1
pagerank20largest_count_score = pagerank20largest_list[w]
pagerank20largest_count_score = pagerank20largest_count_score_w1.reset_index()
pagerank20largest_count_score.rename(columns={'index':'user_id'}, inplace=True)
pagerank20largest_count_score['page_rank']=1


malicious_users = pd.merge(hs_freq20largest_count_score, postfreq20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, hsratio20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, av_overperforming20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, betweenness20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, degreecentrality20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, eigenvector20largest_count_score, how='outer', on='user_id')
malicious_users = pd.merge(malicious_users, pagerank20largest_count_score, how='outer', on='user_id')

malicious_users = malicious_users.fillna(0)



malicious_users['malicious_score'] = (malicious_users['hs_freq']/(malicious_users['hs_freq']+0.00001))*(malicious_users['hs_freq']+malicious_users['postfreq']+malicious_users['hsratio']+malicious_users['degree_centrality']+malicious_users['page_rank'])
malicious_users = malicious_users.sort_values(by=['malicious_score'], ascending=False)
malicious_users = malicious_users.round()

malicious_users['week'] = '12/10/2020' #change this

#change file path
malicious_users.to_csv(r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Dashboard\Sample data for dashboard\malicioususers_week17.csv')