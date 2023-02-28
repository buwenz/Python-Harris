# PPHA 30535
# Spring 2022
# Homework 4 and 5

# Buwen Zhang

# Buwen Zhang
# buwenz

# Due date: Sunday May 8th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work. Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the two csv documents included in
# your repo.  In nst-est2019-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, 20 is a US region, and 40 is a US state. REGION
# is the fips code for the US region. STATE is the fips code for the US state
# The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nst-est2019-alldata.pdf
# Note that each question will build on the modified dataframe from the
# question before.

# Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.  Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.
import os
import pandas as pd

path = os.getcwd()
print(path) #the base path is r'/Users/lindsey/Desktop/homework-4-and-5-buwenz'
dataframe = pd.read_csv(path + '/nst-est2019-alldata.csv')
df_visit = pd.read_csv(path + '/state-visits.csv')

#Explore the data (I discussed this part with Bihter Erbas)
#First describe the data:
dataframe.describe()

#see what rows this dataframe has:
print(dataframe.head())

#see what columns this dataframe has:
print(dataframe.columns.tolist()) #from: https://stackoverflow.com/questions/49188960/how-to-show-all-columns-names-on-a-large-pandas-dataframe

#group by reginal levels and find the means
print(dataframe.groupby('SUMLEV').groups)

# Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.
import us
abbr2fips = us.states.mapping('abbr','fips')
print(abbr2fips)

fips2abbr = {}
tmp = us.states.mapping('fips','abbr')
print(tmp)
for keys in tmp:
    if keys is not None:
        fips2abbr[int(keys)] = tmp[keys]
# Question 3: Subset the data so that only observations for individual
# US states remain, and only state names and data for the population
# estimates in 2010-2019 remain.
indices = []
for ind in dataframe.columns:
    if ind == 'STATE' or ind.startswith('POPESTIMATE'):
        indices.append(ind)

dataframe = dataframe[dataframe.SUMLEV == 40].loc[:, indices]
for index, row in dataframe.iterrows():
    dataframe.loc[index, 'STATE'] = fips2abbr[dataframe.loc[index, 'STATE']]
print(dataframe)
print(indices)

# Question 4: Reshape the data from wide to long, making sure you reset
# the index to the default values if any of your data is located in the index.
dataframe = pd.wide_to_long(dataframe, stubnames=['POPESTIMATE',], j='year', i='STATE')
print(dataframe)

# Question 5: Open the state-visits.csv file, and fill in the VISITED column
# with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the file as a dataframe in
# Python, and merge the visited column into your population dataframe, only
# keeping values that appear in both dataframes.  Are any observations
# dropped from this?  Show code where you investigate your merge, and
# display any observations that weren't in both dataframes.
df_visit = pd.read_csv(path + '/state-visits.csv')
df_merge = dataframe.merge(df_visit, on=['STATE'], how='inner')

df_unvisit = dataframe.merge(df_visit, on=['STATE'], how='left')
dropped_states = df_unvisit[df_unvisit.VISITED.isna()]
print(dropped_states)

#another thought on how to validate dropped data
valid_state = []
for index, row in df_visit.iterrows():
    state, visited = row['STATE'], row['VISITED']
    if visited == True:
        valid_state.append(state)

print(valid_state)

dataframe.loc[:, 'VISITED'] = False
dataframe.loc[valid_state, 'VISITED'] = True
print(dataframe)
dropped_states = dataframe[dataframe.VISITED==False]
print(dropped_states)