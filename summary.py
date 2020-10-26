# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:07:58 2020

@author: Anna
"""

## Summary statistics for dashboard

# Load window

total_number_of_posts = window['post_url'].nunique()

total_number_of_comments = len(window)

number_of_hs_comments = len(window[(window['hate_speech']==True)])

percentage_hate_speech = number_of_hs_comments/total_number_of_comments*100

total_number_of_unique_users = window['user_id']
