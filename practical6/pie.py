import matplotlib.pyplot as plt
#Pie chart, where the slices will be ordered and plotted counter-clockwise:
#set a new frequency dictionary
Countries = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
#compute the total number
total=sum(list(Countries.values()))
#compute the frequency
frequency={k:m/total*100 for k, m in Countries.items()}
#make the pie chart
sizes = list(frequency.values())
countries = list(frequency.keys())
#give sides and labels
plt.pie(sizes, 
       labels=countries,  
       autopct='%1.1f%%', 
        startangle=90,  
        explode = [0,0,0,0,0],  
        shadow=False  
       )
#give the pie chart's information
plt.axis('equal')
#Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("the proportion of infections")
plt.show()
