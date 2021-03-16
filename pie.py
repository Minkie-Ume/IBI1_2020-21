import matplotlib.pyplot as plt
#Pie chart, where the slices will be ordered and plotted counter-clockwise:
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
countries = ['USA', 'India', 'Brazil', 'Russia', 'UK']
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes, 
       labels=countries,  
       autopct='%1.1f%%', 
        startangle=90,  
        explode = [0,0,0,0,0],  
        shadow=False  
       )
plt.axis('equal')
#Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("the proportion of infections")
plt.show()
