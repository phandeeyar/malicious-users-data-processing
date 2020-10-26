# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:45:54 2020

@author: Anna
"""

### Master data cleaning file

#Load required packages and files
import pandas as pd
import numpy as np

#These are always the same files:
lexicon = pd.read_excel(r'C:/Users/Anna/Documents/Consulting opportunities/Phandeeyar/Project files/Data/cleaned data/200825lexiconcleaned.xlsx')
electiontopics_outputfilepath = r'C:/Users/Anna/Documents/Consulting opportunities/Phandeeyar/Project files/Data/cleaned data/electiontopickeywords.xlsx'

#These files need to be changed for every week
inputfilepath = r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Data\from server\20201015_20201019\*.xlsx'
outputfilepath = 'C:/Users/Anna/Documents/Consulting opportunities/Phandeeyar/Project files/Data/cleaned data/from server/week 1015_1019/1015_1019_pagecommentsmerged.xlsx'
procdata = pd.read_csv(r'C:/Users/Anna/Documents/Consulting opportunities/Phandeeyar/Project files/Data/from server/processed comments pages overview/20201015_20201019.csv', sep='~')

#ID for the folder, this needs to be changed for every week
folder_name = 'f1015' 


# Step 1: Import comments data from all the excel files with user comments

def import_comments_data(inputfilepath, outputfilepath):
    columns = ['Comment ID', 'Reply ID', 'User Name', 'Profile ID', 'Date', 'Likes', 'Comment', 'Link']
    df = pd.DataFrame(columns=columns)
    
    import glob
    
    for filepath in glob.iglob(inputfilepath):
        dfnew = pd.read_excel(filepath)
        link = dfnew.get_value(0, 'Unnamed: 1')
        dfnew=dfnew.drop(dfnew.index[0:5])
        dfnew.columns = ['Comment ID', 'Reply ID', 'User Name', 'Profile ID', 'Date', 'Likes', 'Comment', 'View Source']
        dfnew['Link'] = link
        dfnew=dfnew.drop(columns=['View Source'])
        df = pd.concat([df,dfnew])
        
    df.rename(columns={'Profile ID':'profile_id', 'Comment ID':'comment_id', 'Reply ID':'reply_id', 'User Name':'user_name', 'Date':'date', 'Likes':'likes', 'Comment':'comment', 'Link':'post_url'}, inplace=True)
    df = df[['post_url', 'comment_id', 'reply_id', 'profile_id', 'user_name', 'date', 'comment', 'likes']]
    df['profile_id'] = df['profile_id'].str[3:] #delete ID: from profile_id for better matching
    df['profile_id'] = df['profile_id'].str.replace(" ","") #remove empty spaces in profile_id column
        
    # create unique user_id consisting of user_name and profile_id
    df.dtypes
    df["user_id"] = df["user_name"].astype(str) + ' '+ df["profile_id"].astype(str)
    df['post_type'] = df['post_url'].str.contains('groups', na=False) # add post type (group vs. page)
    df['post_type'].replace({True:'group', False:'page'}, inplace=True)
    df['row_number']=np.arange(len(df))
    df['row_id'] = folder_name +' '+ df['row_number'].astype(str)
    del df['row_number']
    
    df['post_url']= folder_name + ' '+ df['post_url'].astype(str)
    
    return df

df = import_comments_data(inputfilepath, outputfilepath)    



# Step 2: label hate speech comments

def label_hate_speech(df, lexicon, outputfilepath):
    df['hate_speech'] = df['comment'].str.contains('|'.join(lexicon['label'].values), na=False)
    
    return df

df = label_hate_speech(df, lexicon, outputfilepath)

    

##############################################################################
# SECTION 4: ADDING PROCESSED DATA INFORMATION TO DF

# Required: Processed data file
# Output: Clean processed data file, post information added to df

### for groups
procdatasubset = procdata[['Group Name', 'User Name', 'Likes at Posting', 'Type', 'Likes', 'Comments', 'Shares', 'Angry', 'URL', 'Link', 'Overperforming Score']]
procdatasubset['URL'] = folder_name +' '+ procdatasubset['URL'].astype(str)
procdatasubset['Link'] = folder_name +' '+ procdatasubset['Link'].astype(str)

procdatasubset.rename(columns={'Group Name':'group_name', 'User Name':'page_user_name','Likes at Posting':'page_likes_at_posting','Type':'media_type','Likes':'post_likes','Comments':'comments','Shares':'shares','Angry':'angry_reactions','URL':'post_url','Link':'media_link','Overperforming Score':'overperforming_score'}, inplace=True)
df = pd.merge(df, procdatasubset, on='post_url', how='left')


del procdata
del procdatasubset




##############################################################################
# SECTION 7: ADD HATE SPEECH TARGETS

def add_hs_targets(df, lexicon, outputfilepath):
    lexicontargets = lexicon['targetted_group'].value_counts()
    lexicontopiclist = lexicon.set_index('label')['targetted_group']

    #column with found hate speech items
    found2 = (df["comment"].str.extractall("|".join(f"(?P<label{num}>{i})" for num, i in enumerate(lexicontopiclist.index, 1))).groupby(level=0).first())

    def squeeze_nan(x, hold):
        if x.name not in hold:
            original_columns = x.index.tolist()

            squeezed = x.dropna()
            squeezed.index = [original_columns[n] for n in range(squeezed.count())]

            return squeezed.reindex(original_columns, fill_value=np.nan)
        else:
            return x

    found2 = found2.apply(lambda x: squeeze_nan(x, ['B']), axis=1)
    found2 = found2[['label1','label2','label3','label4']]

    lexicontopiclist = lexicontopiclist.reset_index()
    lexicontopiclist = lexicontopiclist.drop_duplicates(subset=['label'], keep='first')

    dfmergefound = pd.merge(df, found2, how='left', left_index=True, right_index=True)

    lexicontopiclist.columns = ['label1','targeted_group1']
    dfmergefoundtopic = pd.merge(dfmergefound, lexicontopiclist, how='left', on='label1')

    lexicontopiclist.columns = ['label2','targeted_group2']
    dfmergefoundtopic = pd.merge(dfmergefoundtopic, lexicontopiclist, how='left', on='label2')

    lexicontopiclist.columns = ['label3','targeted_group3']
    dfmergefoundtopic = pd.merge(dfmergefoundtopic, lexicontopiclist, how='left', on='label3')

    lexicontopiclist.columns = ['label4','targeted_group4']
    dfmergefoundtopic['label4'] = dfmergefoundtopic['label4'].astype(str)
    dfmergefoundtopic = pd.merge(dfmergefoundtopic, lexicontopiclist, how='left', on='label4')

    dfmergefoundtopic.rename(columns={'label1':'hate_speech_item1', 'label2':'hate_speech_item2', 'label3':'hate_speech_item3', 'label4':'hate_speech_item4'}, inplace=True)


    return dfmergefoundtopic

df = add_hs_targets(df, lexicon, outputfilepath)

##############################################################################
## SECTION 8: ADD ELECTION TOPICS TO COMMENTS

def add_election_topic_from_hs(df, outputfilepath):
    # political parties
    df.loc[(df['targeted_group1']=='USDP')|(df['targeted_group1']=='NLD')|(df['targeted_group1']=='Tatmadaw/USDP')|(df['targeted_group1']=='USDP MPs')|(df['targeted_group1']=='Government'),'election_topic']=True
    df.loc[(df['targeted_group2']=='USDP')|(df['targeted_group2']=='NLD')|(df['targeted_group2']=='Tatmadaw/USDP')|(df['targeted_group2']=='USDP MPs')|(df['targeted_group2']=='Government'),'election_topic']=True
    df.loc[(df['targeted_group3']=='USDP')|(df['targeted_group3']=='NLD')|(df['targeted_group3']=='Tatmadaw/USDP')|(df['targeted_group3']=='USDP MPs')|(df['targeted_group3']=='Government'),'election_topic']=True
    df.loc[(df['targeted_group4']=='USDP')|(df['targeted_group4']=='NLD')|(df['targeted_group4']=='Tatmadaw/USDP')|(df['targeted_group4']=='USDP MPs')|(df['targeted_group4']=='Government'),'election_topic']=True

    # Covid-19
    df.loc[(df['targeted_group1']=='Chinese')|(df['targeted_group1']=='Ethnic minority/ Migrant workers')|(df['targeted_group1']=='Migrant workers')|(df['targeted_group1']=='Prisoner'), 'election_topic']==True
    df.loc[(df['targeted_group2']=='Chinese')|(df['targeted_group2']=='Ethnic minority/ Migrant workers')|(df['targeted_group2']=='Migrant workers')|(df['targeted_group2']=='Prisoner'), 'election_topic']==True
    df.loc[(df['targeted_group3']=='Chinese')|(df['targeted_group3']=='Ethnic minority/ Migrant workers')|(df['targeted_group3']=='Migrant workers')|(df['targeted_group3']=='Prisoner'), 'election_topic']==True
    df.loc[(df['targeted_group4']=='Chinese')|(df['targeted_group4']=='Ethnic minority/ Migrant workers')|(df['targeted_group4']=='Migrant workers')|(df['targeted_group4']=='Prisoner'), 'election_topic']==True

    df['election_topic'] = df['election_topic'].fillna(False)
    
    return df

df = add_election_topic_from_hs(df, outputfilepath)



##############################################################################
## SECTION 9: ADD NUMBER OF POSTS A USER HAS MADE

def add_number_of_posts(df, outputfilepath):
    frequentusers = df['user_id'].value_counts()
    frequentusers = frequentusers.reset_index()
    frequentusers.rename(columns={'index':'user_id', 'user_id':'number_of_posts'}, inplace=True)
    df = pd.merge(df, frequentusers, how='left', on='user_id')
    
    return df

df = add_number_of_posts(df, outputfilepath)


##############################################################################
## Section 10: Add election topics


electiontopics = pd.read_excel(r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Data\hate speech lexicon\Lexicon.xlsx', sheet_name='topic')
electiontopics_outputfilepath = r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Data\cleaned data\electiontopickeywords.xlsx'

def add_election_topics_from_keywords(df, electiontopics, electiontopics_outputfilepath, outputfilepath):
    electiontopics = electiontopics[(electiontopics['party/elections'].notna())|(electiontopics['covid'].notna())]
    electiontopics = electiontopics.drop(columns=['religion', 'ethnic', 'armed conflict', 'activism'])
    electiontopics['election_topic'] = True
    electiontopics['party/elections'] = electiontopics['party/elections'].replace({'x':True, np.nan:False})
    electiontopics['covid'] = electiontopics['covid'].replace({'x':True, np.nan:False})
    electiontopics = electiontopics.rename(columns={'topic':'keyword'})
    electiontopics = electiontopics.reset_index(drop=True)
    electiontopics.to_excel(electiontopics_outputfilepath)
    #df['hate_speech'] = df['comment'].str.contains('|'.join(lexiconall['label'].values), na=False)
    df['hate_speech'] = df['comment'].str.contains('|'.join(lexicon['label'].values), na=False)
    df['election_topic3'] = np.nan
    df['election_topic2'] = df['comment'].str.contains('|'.join(electiontopics['keyword'].values), na=False)
    df.loc[(df['election_topic']==True) | df['election_topic2']==True, 'election_topic3'] = True
    df.rename(columns={'election_topic':'election_topic_hs', 'election_topic2':'election_topic_keyword', 'election_topic3':'election_topic'}, inplace=True)
    df['election_topic'] = df['election_topic'].replace({np.nan:False})
   
    return df

df = add_election_topics_from_keywords(df, electiontopics, electiontopics_outputfilepath, outputfilepath)

df['overperforming_score'] = df['overperforming_score'].astype(str).replace(',','')
df['overperforming_score'] = df['overperforming_score'].str.replace(",","")
df['overperforming_score'] = df['overperforming_score'].astype(float)




################################################################################

def mark_duplicate_comments(df):
    duplicatecomments = df[(df['hate_speech'] == True)]
    duplicatecomments = duplicatecomments[duplicatecomments.duplicated('comment', keep=False)]
    duplicatecomments = duplicatecomments.dropna(subset=['comment'])
    duplicatecomments = duplicatecomments.sort_values(by=['comment'])

    # drop comments that are equal to hate speech items
    duplicatecomments.drop(duplicatecomments[duplicatecomments['comment']==duplicatecomments['hate_speech_item1']].index, inplace=True)
    duplicatecomments['comment_length'] = duplicatecomments['comment'].str.len()
    duplicatecomments = duplicatecomments.drop(duplicatecomments[(duplicatecomments.comment_length <10)].index)
    duplicatecomments['double_comment'] = True
    doublecomments = duplicatecomments[['row_id','double_comment']]
    df = pd.merge(df, doublecomments, on='row_id', how='left')
    df['double_comment'] = df['double_comment'].fillna(False)
    
    return df

df = mark_duplicate_comments(df)


df.to_excel(outputfilepath)