import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import libiraries, to allow us to work with mathematial functions,files and directories,dataframes.

os.chdir("/Users/minkie/IBI1_2020-21/practical7")
covid_data = pd.read_csv("full_data.csv")
#read the content of the .csv file into a dataframe object.

covid_data.iloc[0:10:2,:]
#showing all columns, and every second row between 0 and 10.

row=[]#creat a new list for boolean.
for i in range (0,7996):
	if covid_data.loc[i,"location"]=="Afghanistan":
		row.append(True)
	else:
		row.append(False)#giving boolean to the list

covid_data.loc[row,"total_cases"]

new=[]
for i in range (0,7996):
	if covid_data.loc[i,"location"]=="World":
		new.append(True)
	else:
		new.append(False)

covid_data.loc[new,"new_cases"]#seperate world's data from the file.

np.mean(covid_data.loc[new,"new_cases"])
#calculate the mean of the data is 8454.326086956522
np.median(covid_data.loc[new,"new_cases"])
#calculate the median of the data is 2023.5

world_new_cases= covid_data.loc[new,"new_cases"]#get the range of data
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(world_new_cases)
plt.show()

world_new_cases= covid_data.loc[new,"new_cases"]
world_new_deaths= covid_data.loc[new,"new_deaths"]
world_dates= covid_data.loc[new,"date"]
#create x-axis and y-axis
plt.plot(world_dates, world_new_cases,'b+')
plt.plot(world_dates, world_new_deaths,'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#making the figure better
#create figure
plt.show()

date=[]#creat a new list for boolean.
for i in range (0,7996):
        if covid_data.loc[i,"date"]=="2020-03-14":
                date.append(True)
        else:
                date.append(False)#giving boolean to the list

fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(covid_data.loc[date,"total_cases"])
plt.show()

