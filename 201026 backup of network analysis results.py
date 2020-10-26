# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:21:22 2020

@author: Anna
"""
import os
os.getcwd()
os.chdir(r'C:\Users\Anna\Documents\Consulting opportunities\Phandeeyar\Project files\Backup\Results')

import pickle
file_name = "oneweekwindows.pkl"
open_file = open(file_name, "wb")
pickle.dump(window_list, open_file)
open_file.close()

#open_file = open(file_name, "rb")
#loaded_list = pickle.load(open_file)
#open_file.close()
##

file_name = "user_dict_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(user_dict_list, open_file)
open_file.close()


file_name = "hatespeech_dict_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(hatespeech_dict_list, open_file)
open_file.close()


file_name = "election_dict_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(election_dict_list, open_file)
open_file.close()


file_name = "G_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(G_list, open_file)
open_file.close()


file_name = "centrality_measures_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(centrality_measures_list, open_file)
open_file.close()


file_name = "hsusersfreq_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(hsusersfreq_list, open_file)
open_file.close()


file_name = "hs_frequency20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(hs_frequency20largest_list, open_file)
open_file.close()


file_name = "postfreq_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(postfreq_list, open_file)
open_file.close()


file_name = "postfreq20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(postfreq20largest_list, open_file)
open_file.close()


file_name = "hsratio_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(hsratio_list, open_file)
open_file.close()


file_name = "hsratio20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(hsratio20largest_list, open_file)
open_file.close()


file_name = "av_overperforming_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(av_overperforming_list, open_file)
open_file.close()


file_name = "av_overperforming20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(av_overperforming20largest_list, open_file)
open_file.close()


file_name = "degreecentrality20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(degreecentrality20largest_list, open_file)
open_file.close()


file_name = "betweenness20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(betweenness20largest_list, open_file)
open_file.close()


file_name = "eigenvector20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(eigenvector20largest_list, open_file)
open_file.close()


file_name = "pagerank20largest_list.pkl"
open_file = open(file_name, "wb")
pickle.dump(pagerank20largest_list, open_file)
open_file.close()