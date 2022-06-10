# -*- coding: utf-8 -*-
"""
Created on Thur Apr 22 13:15:35 2021

@author: artem
"""
 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#My data merge
df1 = pd.read_csv('C:/Users/nicko/Downloads/my_python/nypd_crimes.csv')
df2 = pd.read_csv('C:/Users/nicko/Downloads/my_python/nypd.csv')
sub_df1 = df1[['PRECINCT', 'AGE', 'SEX', 'RACE']]
sub_df2 = df2[['PRECINCT', 'AGE', 'SEX', 'RACE']]

merged_df = sub_df1.append(sub_df2)

merged_df.head()
print(merged_df.head)

print()
merged_df.shape
print(merged_df.shape)

#Merged- Checks out with the  same number of rows as  my 'newoutput.csv'
merged_df.dtypes
print(merged_df.dtypes)

print()

#Beggining of my Analysis
merged_df['PRECINCT'].value_counts()
print(merged_df)

print()

#Precinct and ages of arrest types using bound method .groupby for this <<<<<
merged_df.groupby(['PRECINCT','AGE'])['RACE'].count()
print(merged_df.groupby)

print()
#group by race
merged_df.groupby(['PRECINCT','RACE'])['AGE'].count()

print()
print("==============================================================")
print("ANALYSIS START FOR 123 PRECINCT...")
#ANALYSIS of 123rd PRECINCT BELOW followed be value_counts
merged_df[merged_df['PRECINCT'] == 123].value_counts()
#Making sure preceinc,t age, asex, race below is there
precinct_123 = merged_df[merged_df['PRECINCT'] == 123]
print(precinct_123.shape)
print(type(precinct_123))
print(precinct_123.columns)

#I will attempt to plot precinct 123's AGE group by assigning it value of x then using plt.hist
x = precinct_123['AGE']
plt.hist(x)

#Attempting simiiar but by Sex this time instead of Age 
y = precinct_123['SEX']
y = y.astype(str)
plt.hist(y)

print("I am able to tell the following based of precinct 123 data")
print("Precinct 123 highest offender arrest rate by sex is Male group")
print("Precinct 123 highest offender arrest rate by age is 25-44 group")

print()
print("==============================================================")

#Below is new code for visualization < ===========================================================================================================

#I want to start by doing a visualization on Age first establishing my merged_df for age below
merged_df['AGE'].value_counts()
#**CHECK** Screenshot #1 to see above merged_df for Age it is the same as the data below:
Age = ['<18', '18-24', '25-44', '45-64', '65+', 'UNKNOWN']
Arrests = [7109, 38726, 93918, 31935, 2171, 22142]

#Let me plot the Arrests by Age Across NYC below decided to go with the simple bar graph:
#**CHECK** Screenshot #2 to see above merged_df for AGE it is the same as the data below:
plt.bar(Age, Arrests)
plt.xlabel('Age')
plt.ylabel('Number of Total Arrests')
plt.title('Arrests by Age Across NYC');

print()
print("==============================================================")

#Since I now finished Age I want to check Race across NYC 
merged_df['RACE'].value_counts()
#**CHECK** Screenshot #3 to see above merged_df for RACE it is the same as the data below:
race = ['Black', 'White Hispanic', 'White', 'Black Hispanic', 'Asian / Pacific Islander', 'American Indian/Alaskan Native', 'UNKOWN', 'OTHER']
num_arrests = [85454, 42486, 19115, 15782, 8941, 605, 1372, 222]    

#**CHECK** Screenshot #4 to see above merged data for RACE in my chart:
plt.barh(race, num_arrests)
plt.xlabel('Number of Arrests')
plt.ylabel('Race')
plt.title('Arrests by Race Across NYC');

print()
print("==============================================================")

# I have now been able to establish two charts
# 1 chart for AGE of arrests ACROSS NYC
# 2nd chart for RACE number of arrests ACROSS NYC


#------------------- Now I want to use my combined data of specically the following races: White & Black according to my CSV
#------------------- To be able to establish a chart that will show me the NUM OF ARRESTS OF BLACK & WHITE PEOPLE IN NYC

#Below I am creating black_df pulling it from my merged_df from specifcally race being black
black_df = merged_df[merged_df['RACE'] == 'BLACK']
#Below I am creating black_df pulling it from my merged_df from specifcally race being white
white_df = merged_df[merged_df['RACE'] == 'WHITE']

#I want to quickly see the arrest numbers by age groups below:
    
black_df['AGE'].value_counts()
white_df['AGE'].value_counts()
#**CHECK** Screenshot #5 to see above table data which is the same as the data below:
age = ['<18', '18-24', '25-44', '45-64', '65+', 'UNKNOWN']
bl_arrests = [4376, 20127, 44590, 15416, 883, 62]
wh_arrest = [301, 2734, 11022, 4616, 425, 17]

#Setting up chart below initally it was a bit messy so some cleanup needed to be done
x = np.arange(len(age))
width = .35
#Assigning my races to their specific bars
fig, ax = plt.subplots()
bl = ax.bar(x - width/2, bl_arrests, width, label = 'Black')
wh = ax.bar(x + width/2, wh_arrest, width, label = 'White')

#**CHECK** Screenshot #6 to see the chart below:
ax.set_ylabel('Number of Arrests')
ax.set_title('Number of Arrests of Black and White New Yorkers')
ax.set_xticks(x)
ax.set_xticklabels(age)
ax.legend()
fig.tight_layout()
plt.show()

print()
print("==============================================================")
