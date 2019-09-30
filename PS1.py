#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""
#Students:
#Nichole Bouffard
#Corey Loo
#Nick Hoang
#Ariana Giuliano

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
adult1 = 'hello world! python line ' + '1' 
print(adult1)

# second group member's error to fix
a = [1, 3, 'a']
baby1 = a[2]

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
spider = 1.0
bite = 'ouch'
coder3 = str(spider)+str(bite)


# Fourth group member's error to fix
for i in [1,2,-3,4,-5]:
    if i > 0:
        print('positive')
    else:
        print('negative')
coder4= print(I)

# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt.index(-1)

# and then use missing_rt to remove the trial from rt
del(rt[missing_rt])
clean_rt = rt

# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]

# try the same procedure. Does it work? 
# use a comment to explain why or why not below in comments
missing_rts = rt_trouble.index(-1)
# this only indexes and removes the first missing value

# now write an if statement that you can use to remove the frist missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.

# The question asks to use an if statement
#clean_rt = rt_trouble
#while -1 in clean_rt:
#   missing_rt = rt_trouble.index(-1)
#   del(rt_trouble[missing_rt])
    
if -1 in rt_trouble:
    missing_rt = rt_trouble.index(-1)
    del(rt_trouble[missing_rt])
    clean_rt=rt_trouble
    print('missing values removed')      
else:
    clean_rt=rt_trouble


# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

if -1 in data[0]:
  for x in data[0]:
    if x < 0:
        missing = data[0].index(-1)
        del(data[0][missing])
        del(data[1][missing])
        del(data[2][missing])
        clean_data=data
    else:
        print('missing values removed')
else:
    clean_data=data
