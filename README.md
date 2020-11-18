# Description of files in hate_speech_analysis

# Step 1: Data cleaning
# Run either '201026 data cleaning file final_pages.py' if cleaning pages or '201026 data cleaning file final_groups.py' if cleaning groups. The dashboard contains the data for pages.
# You will need to change the inputfilepath, outputfilepath and the procdata in lines 19 to 21. The inputfilepath is the folder that you want to clean. The outputfilepath is where you want to save the cleaned data. The procdata is the csv that contains the processed data for the folder. You will also need to change the folder_name in line 24 to the date of the folder. This creates an identifier called row_id in each row that shows which folder the data comes from and makes it easier to check for duplicate rows.
# In case there is an error running the files, check if the first loop in line 35-42 works. Some of the folders from the AWS had corrupted files, which interrupted the loop. If the loop doesn't work, run '201118 find corrupted file in folder.py' using the same input filepath. This loop has a counter and will show you which file is causing trouble to import. If the counter stops at 218 for example, you will need to manually go into the folder and try to open the 218th. If it is corrupted, remove it from the folder. Repeat until there are no issues. If there are any other errors when running the data cleaning code, please email me and I will help you.

# Step 2: Create the rolling window for the analysis
# Run '201026 rolling window creation.py'. This creates the rolling windows for the network analysis. The inputfilepath for this file is the outputfilepath from step 1. The loop combines folder1+folder2, folder2+folder3, folder3+folder4 and so on and saves them in a list. So if you want to access all the comments data for the first week, you will need to call window_list[0], for the second week window_list[2] and so on. If you are in doubt, check the row_id to see if the window that you selected contains the data for the correct week.

# Step 3: Conduct the network analysis
# Now the exciting part starts. '201026 network analysis.py' contains the code to conduct the actual analysis. First, all the functions required for the network analysis are defined and then they are applied on each window in the window_list. This file will take a very long time to run, depending on the amount of data you have, it can run for more than 14 hours. The run time is so long because it takes a long time to calculate the centrality measures. There is a counter in the loop and the name of the individual steps are also printed to show progress. For some windows, calculating the centrality measures may take more than 2 hours because of the amount of data, so be patient and don't exit the program thinking that your computer froze. The output of the functions are saved in lists after the code finishes running and can easily be accessed in case you are looking for information on a specific window.

# Step 4: Backup the results of the network analysis
# Because the run time of the network analysis code is so long, it is important to save the results before proceeding. Run '201026 backup of network analysis results.py' when the network analyis code finishes. This saves the lists using pickle_dump.

# Step 5: Calculate the overall malicious user scores
# Run '201026 overall malicious user score calculation.py' using the lists created in step 3 to calculate the overall malicious user scores. Change line 179 to save your results locally or on the server.

# Step 6: Calculate the malicious user scores for the particular week
# Run '201118 malicious user one week.py' to calculate the malicious user scores for a particular week. Changes you need to make: line 9: change w to the week or window you want to access, in line 57 change the date to the start date of the week you want to display and in line 60 change the filepath to the location where you want to save your results.
