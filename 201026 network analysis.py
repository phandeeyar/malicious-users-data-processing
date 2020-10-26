# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:19:13 2020

@author: Anna
"""

## Network setup functions

import pandas as pd
import numpy as np

# Step 1: Define functions

def create_user_dict(networkdf):
    networkdf = networkdf[['comment_id', 'reply_id', 'user_id', 'hate_speech']]
    # Create columns for posters and respondents
    networkdf['poster'] = networkdf.user_id.mask(networkdf.comment_id.isna())
    networkdf['respondent'] = networkdf.user_id.mask(networkdf.reply_id.isna())
    networkdfuser = networkdf[['poster','respondent']]
    networkdfuser['poster'] = networkdfuser['poster'].fillna(method='ffill')
    networkdfuser = networkdfuser.dropna(subset=['respondent'])
    user_dict = {k: g["respondent"].tolist() for k,g in networkdfuser.groupby("poster")}
    
    return user_dict


########################################################################
def create_hatespeech_dict(networkdf):
    networkdf = networkdf[['comment_id','reply_id','user_id','hate_speech']]
    #networkdf = networkdf[(networkdf['hate_speech']==True)]
    networkdf['poster'] = networkdf.user_id.mask(networkdf.comment_id.isna())
    networkdf['respondent'] = networkdf.user_id.mask(networkdf.reply_id.isna())
    # Prepare the second df to get unique hate speech users
    userunique = networkdf['user_id'].value_counts()
    userunique = userunique.reset_index()
    userunique.rename(columns={'index':'user_id','user_id':'post_number'}, inplace=True)
    hatespeechusers = networkdf[(networkdf["hate_speech"]==True)]
    
    hatespeechusers = hatespeechusers.reset_index(drop=True)
    hatespeechusers['poster']=hatespeechusers.user_id.mask(hatespeechusers.comment_id.isna())
    hatespeechusers['respondent']=hatespeechusers.user_id.mask(hatespeechusers.reply_id.isna())
    
    userunique = pd.merge(userunique, hatespeechusers, on='user_id', how='left')
    userunique.loc[userunique.hate_speech.isna(), 'hate_speech'] = False
    hatespeech_dict = userunique.set_index('user_id')['hate_speech'].to_dict()
    
    return hatespeech_dict
    

##############################################################################
def create_election_dict(networkdf):
    networkdf = networkdf[['comment_id','reply_id','user_id','election_topic']]
    networkdf['poster'] = networkdf.user_id.mask(networkdf.comment_id.isna())
    networkdf['respondent'] = networkdf.user_id.mask(networkdf.reply_id.isna())
    
    # Prepare the second df to get unique users talking about elections
    userunique = networkdf['user_id'].value_counts()
    userunique = userunique.reset_index()
    userunique.rename(columns={'index':'user_id','user_id':'post_number'}, inplace=True)
    electionusers = networkdf[(networkdf["election_topic"]==True)]
    
    electionusers = electionusers.reset_index(drop=True)
    electionusers['poster']=electionusers.user_id.mask(electionusers.comment_id.isna())
    electionusers['respondent']=electionusers.user_id.mask(electionusers.reply_id.isna())
    
    userunique = pd.merge(userunique, electionusers, on='user_id', how='left')
    userunique.loc[userunique.election_topic.isna(), 'election_topic'] = False
    election_dict = userunique.set_index('user_id')['election_topic'].to_dict()
    
    return election_dict


#########################################################################
import networkx as nx

def create_comments_graph(user_dict):
    G = nx.Graph()
    for i, j in user_dict.items():
        for k in j:
            G.add_edge(i,k)

    return G


##############################################
def calculate_centrality_measures(G):
    degree_centrality = nx.degree_centrality(G) #returns dictionary
    centrality_measures = pd.DataFrame.from_dict(degree_centrality, orient='index')
    centrality_measures.columns =['degree_centrality']
    
    betweenness_centrality = nx.betweenness_centrality(G)
    betweenness_centrality = pd.DataFrame.from_dict(betweenness_centrality, orient='index')
    betweenness_centrality.columns = ['betweenness_centrality']
    centrality_measures = pd.merge(centrality_measures, betweenness_centrality, left_index=True, right_index=True)
    
    eigenvector_centrality = nx.eigenvector_centrality_numpy(G)
    eigenvector_centrality = pd.DataFrame.from_dict(eigenvector_centrality, orient='index')
    eigenvector_centrality.columns = ['eigenvector_centrality']
    centrality_measures = pd.merge(centrality_measures, eigenvector_centrality, left_index=True, right_index=True)
    
    page_rank = nx.pagerank(G)
    page_rank = pd.DataFrame.from_dict(page_rank, orient='index')
    page_rank.columns = ['page_rank']
    centrality_measures = pd.merge(centrality_measures, page_rank, left_index=True, right_index=True)
    
    return centrality_measures


###############################################################################    
def most_central_users(centrality_measures):
    highest_degree_centrality = centrality_measures.degree_centrality.argmax()
    highest_betweenness_centrality = centrality_measures.betweenness_centrality.argmax()
    highest_eigenvector_centrality = centrality_measures.eigenvector_centrality.argmax()
    highest_page_rank = centrality_measures.page_rank.argmax()
    data = {'centrality_measures':['highest_degree_centrality','highest_betweenness_centrality','highest_eigenvector_centrality','highest_page_rank'],
            'most_central_user':[highest_degree_centrality, highest_betweenness_centrality, highest_eigenvector_centrality, highest_page_rank]}
    df = pd.DataFrame(data, columns = ['centrality_measures', 'most_central_user'])
    
    return df


###############################################################################
def get_hs_frequency(df):
    hsusers = df[(df['hate_speech']==True)]
    hsusersfreq = hsusers['user_id'].value_counts()
    hsusersfreq = hsusersfreq.reset_index()
    hsusersfreq.rename(columns={'index':'user_id','user_id':'hs_count'}, inplace=True)
    
    return hsusersfreq


###############################################################################
def get_hs_frequency20largest(hsusersfreq):
    hs_frequency20largest = hsusersfreq.nlargest(20, ['hs_count'])
    hs_frequency20largest = hs_frequency20largest.sort_values(by=['hs_count'], ascending=False)
    
    return hs_frequency20largest


###############################################################################
def get_postfreq(df):
    postfreq = df['user_id'].value_counts()
    postfreq = postfreq.reset_index()
    postfreq = postfreq.rename(columns={'index':'user_id', 'user_id':'post_count'})
    
    return postfreq


###############################################################################
def get_postfreq20largest(postfreq):
    postfreq20largest = postfreq.nlargest(20, ['post_count'])
    postfreq20largest = postfreq20largest.sort_values(by=['post_count'], ascending=False)

    return postfreq20largest


###############################################################################    
def get_hsratio(postfreq, hsusersfreq):
    hsratio = pd.merge(postfreq, hsusersfreq, how='left', on='user_id')
    hsratio['hs_count'] = hsratio['hs_count'].fillna(0)
    hsratio['hsratio'] = hsratio['hs_count']/hsratio['post_count']
    
    return hsratio


###############################################################################
def get_hsratio20largest(hsratio):
    hsratio20largest = hsratio.nlargest(20, ['hsratio'])
    hsratio20largest = hsratio20largest.sort_values(by=['hsratio'], ascending=False)
    
    return hsratio20largest


###############################################################################
def get_av_overperforming(df):
    av_overperforming = df[['user_id', 'overperforming_score']]
    av_overperforming = av_overperforming.groupby(by=['user_id']).sum()
    av_overperforming = av_overperforming.reset_index()
    av_overperforming = pd.merge(av_overperforming, hsusersfreq, how='left', on='user_id')
    av_overperforming = pd.merge(av_overperforming, postfreq, how='left', on='user_id')
    av_overperforming['av_overperforming'] = av_overperforming['overperforming_score']/av_overperforming['post_count']
    
    return av_overperforming


###############################################################################
def get_av_overperforming20largest(av_overperforming):
    av_overperforming20largest = av_overperforming.nlargest(20, ['overperforming_score'])
    av_overperforming20largest = av_overperforming20largest.sort_values(by=['overperforming_score'], ascending=False)
    
    return av_overperforming20largest


###############################################################################
def get_degreecentrality20largest(centrality_measures):
    degreecentrality20largest = centrality_measures.nlargest(20,['degree_centrality'])
    degreecentrality20largest = degreecentrality20largest[['degree_centrality']]
    degreecentrality20largest = degreecentrality20largest.sort_values(by=['degree_centrality'], ascending=False)
    
    return degreecentrality20largest


###############################################################################
def get_betweenness20largest(centrality_measures):
    betweenness20largest = centrality_measures.nlargest(20, ['betweenness_centrality'])
    betweenness20largest = betweenness20largest[['betweenness_centrality']]
    betweenness20largest = betweenness20largest.sort_values(by=['betweenness_centrality'], ascending=False)
    
    return betweenness20largest


###############################################################################
def get_eigenvector20largest(centrality_measures):
    eigenvector20largest = centrality_measures.nlargest(20, ['eigenvector_centrality'])
    eigenvector20largest = eigenvector20largest[['eigenvector_centrality']]
    eigenvector20largest = eigenvector20largest.sort_values(by=['eigenvector_centrality'], ascending=False)
    
    return eigenvector20largest


###############################################################################
def get_pagerank20largest(centrality_measures):
    pagerank20largest = centrality_measures.nlargest(20, ['page_rank'])
    pagerank20largest = pagerank20largest[['page_rank']]
    pagerank20largest = pagerank20largest.sort_values(by=['page_rank'], ascending=False)
    
    return pagerank20largest


###############################################################################
user_dict_list = []
hatespeech_dict_list = []
election_dict_list = []
G_list = []
centrality_measures_list = []
hsusersfreq_list = []
hs_frequency20largest_list = []
postfreq_list = []
postfreq20largest_list = []
hsratio_list = []
hsratio20largest_list = []
av_overperforming_list = []
av_overperforming20largest_list = []
degreecentrality20largest_list = []
betweenness20largest_list = []
eigenvector20largest_list = []
pagerank20largest_list = []


count = 0
for window in window_list:
    user_dict = create_user_dict(window)
    user_dict_list.append(user_dict)
    print("user_dict")
    hatespeech_dict = create_hatespeech_dict(window)
    hatespeech_dict_list.append(hatespeech_dict)
    print("hatespeech_dict")
    election_dict = create_election_dict(window)
    election_dict_list.append(election_dict)
    print("election_dict")
    G = create_comments_graph(user_dict)
    G_list.append(G)
    print("G_list")
    centrality_measures = calculate_centrality_measures(G)
    centrality_measures_list.append(centrality_measures)
    print("centrality_measures_list")
    hsusersfreq = get_hs_frequency(window)
    hsusersfreq_list.append(hsusersfreq)
    print("hsusersfreq_list")
    hs_frequency20largest = get_hs_frequency20largest(hsusersfreq)
    hs_frequency20largest_list.append(hs_frequency20largest)
    print("hs_frequency20largest_list")
    postfreq = get_postfreq(window)
    postfreq_list.append(postfreq)
    print("postfreq_list")
    postfreq20largest = get_postfreq20largest(postfreq)
    postfreq20largest_list.append(postfreq20largest)
    print("postfreq20largest_list")
    hsratio = get_hsratio(postfreq, hsusersfreq)
    hsratio_list.append(hsratio)
    print("hsratio_list")
    hsratio20largest = get_hsratio20largest(hsratio)
    hsratio20largest_list.append(hsratio20largest)
    print("hsratio20largest_list")
    av_overperforming = get_av_overperforming(window)
    av_overperforming_list.append(av_overperforming)
    print("av_overperforming_list")
    av_overperforming20largest = get_av_overperforming20largest(av_overperforming)
    av_overperforming20largest_list.append(av_overperforming20largest)
    print("av_overperforming20largest_list")
    degreecentrality20largest = get_degreecentrality20largest(centrality_measures)
    degreecentrality20largest_list.append(degreecentrality20largest)
    print("degreecentrality20largest_list")
    betweenness20largest = get_betweenness20largest(centrality_measures)
    betweenness20largest_list.append(betweenness20largest)
    print("betweenness20largest_list")
    eigenvector20largest = get_eigenvector20largest(centrality_measures)
    eigenvector20largest_list.append(eigenvector20largest)
    print("eigenvector20largest_list")
    pagerank20largest = get_pagerank20largest(centrality_measures)
    pagerank20largest_list.append(pagerank20largest)
    print("pagerank20largest_list")
    
    count = count+1
    print(count)