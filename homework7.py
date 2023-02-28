# PPHA 30535
# Spring 2022
# Homework 7

# Buwen Zhang

# Buwen Zhang
# buwenz

# Due date: Sunday May 22nd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data portals for the OECD and the World Bank.  Pick
# any three countries, and pick two data series from each of the OECD and the
# World Bank that covers these places over some time period.  It's ok if
# frequency doesn't match up (e.g. one is monthly and one is quarterly), but
# you will need to handle the aggregation.  Load the data into dataframes using
# Pandas data_reader, then merge the data together in long (tidy) format, and
# write it to a csv document that you commit to your repo.

import pandas as pd
import datetime

import pandas_datareader.data as web
from pandas_datareader import wb
import requests

start = datetime.datetime(2000,1,1)
end = datetime.datetime(2010,12,31)

# for OECD data (I discussed this part with Bihter Erbas)
indicator = 'STI_STEEL_MAKINGCAPACITY'
source = 'oecd'

df_oecd = web.DataReader(indicator, 
                      source,                  
                      start = start,
                      end = end)

df_oecd = df_oecd[['United States', 'Mexico', 'Turkey']]
df_oecd = df_oecd.droplevel([1,2], axis=1).reset_index()

df_oecd = df_oecd.melt(id_vars = 'Year',
                       value_vars = None,
                       var_name = 'country',
                       value_name = 'steel making capacity')
df_oecd['Year'] = df_oecd['Year'].dt.year.astype(str)

# for world bank data
indicator = 'NY.GDP.MKTP.CD'
country=['US', 'MX', 'TR']
start = datetime.datetime(2000,1,1)
end = datetime.datetime(2010,12,31)

df_wb = wb.download(indicator = indicator,
                    country = country,
                    start = start,
                    end = end)
df_wb = df_wb.reset_index()

df_wb.rename(columns = {'year':'Year'}, inplace = True)


df_merged = df_wb.merge(df_oecd, on = ['country', 'Year'], how = 'outer')
df_merged.to_csv('merged.csv')



# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/programs-degrees/degrees/master-public-policy-mpp
# There is a list named Curriculumn after Program Details, explaining the core classes.
# There are 21 bullet points for this, beginning with "Analytical Politics I" and ending
# just before "Elective Options". Some of those bullet points are intented under others. 
# Using requests and BeautifulSoup, collect the text of each of these bullet points so 
# that the top level bullet points, e.g. "Analytical Politics I" are the keys in a 
# dictionary, while the bullet points representing specific classes under them are values
# in a list. The result will be a dictionary where you can index by a requirement and get
# back a list of core class options.

from curses.ascii import BEL
import requests
from bs4 import BeautifulSoup


url = "https://harris.uchicago.edu/academics/degrees/master-public-policy-mpp"

response = requests.get(url)
text = response.text
#print(response.text)
#with open('Master of Public Policy (MPP) _ The University of Chicago Harris School of Public Policy.html', 'r', encoding="utf-8") as page:
#    text=page.read()

text = text.encode('utf-8')
soup = BeautifulSoup(text, 'lxml')
ans = {}
start = False
keys = ["Analytical Politics", "Statistics Sequence", "Microeconomics Sequence"]
tmp_k = None
for i in soup.find_all('p'):
    content = i.text.encode('utf-8').decode('utf-8')
    #print(content)
    if content.startswith("Analytical Politics I"):
        start = True
    if content.startswith('Elective Options'):
        start = False
    if start:
        is_key = False
        for k in keys:
            if content.startswith(k):
                tmp_k = content
                is_key = True
                ans[tmp_k] = []
                break
        if not is_key:
            ans[tmp_k].append(content)



print(ans)

#print(text.encode('utf-8'))