import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import libiraries, to allow us to work with mathematial functions,files and directories,dataframes.

os.chdir("/Users/minkie/IBI1_2020-21/practical7")
#importing the .csv file works
covid_data = pd.read_csv("full_data.csv")
#read the content of the .csv file into a dataframe object.

covid_data.iloc[0:10:2,:]
#showing all columns, and every second row between 0 and 10.

#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
row=[]#creat a new list for boolean.
for i in range (0,7996):
	if covid_data.loc[i,"location"]=="Afghanistan":#if the location is Afghanistan
		row.append(True)#add a True value
	else:
		row.append(False)#add a True value to the list

covid_data.loc[row,"total_cases"]

#computed the mean and median of new cases for the entire world.
new=[]
for i in range (0,7996):
	if covid_data.loc[i,"location"]=="World":
		new.append(True)
	else:
		new.append(False)

covid_data.loc[new,"new_cases"]#seperate world's new cases from the file.
np.mean(covid_data.loc[new,"new_cases"])
#calculate the mean of the data is 8454.326086956522
np.median(covid_data.loc[new,"new_cases"])
#calculate the median of the data is 2023.5

#create a boxplot of new cases
world_new_cases= covid_data.loc[new,"new_cases"]#get the range of data
plt.boxplot(score,
             vert = True,
             whis = 1.5,
             patch_artist = True,
             meanline = False,
             showbox = True,
             showcaps = True,
             showfliers = True,
             notch = False
             )
plt.xlabel('world dates')
plt.ylabel('world new cases')
plt.show()

#plot both new cases and new deaths worldwide.
world_new_cases= covid_data.loc[new,"new_cases"]
world_new_deaths= covid_data.loc[new,"new_deaths"]
world_dates= covid_data.loc[new,"date"]
#create x-axis and y-axis
plt.plot(world_dates, world_new_cases,'b+')
plt.plot(world_dates, world_new_deaths,'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#makes the x-axis looks better
plt.xlabel('dates')
plt.ylabel('cases')
#label x and y axis
plt.show()


#solve my own question
#select the data whose location is China
CHN=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="China":
		CHN.append(True)
	else:
		CHN.append(False)

#collect the data of x-axis and y-axis
China_total_cases=covid_data.loc[CHN,"total_cases"]
China_death_cases=covid_data.loc[CHN,"deaths_cases"]
China_dates=covid_data.loc[CHN,"date"]
plt.plot(China_dates, China_total_cases,'b+')
plt.plot(China_dates, China_death_cases,'b+')
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90)
plt.xlabel('dates')
plt.ylabel('cases')
plt.title('total cases and deaths in China')

