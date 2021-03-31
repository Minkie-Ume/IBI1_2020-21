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
 
