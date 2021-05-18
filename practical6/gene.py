import numpy as np 
import matplotlib.pyplot as plt 
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981]) 
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])
# calculate the average length by dividing one list to the other, then set the average length as a list 
avarage=gene_lengths/exon_counts
L = avarage
#create a list L 
L.sort()
#sorted the list
print(L)
#create a box plot figure
n = 10
scores = L
plt.boxplot(scores,
            vert=True, #boxplot is vertically presented
            whis=1.5, #specifies how far the upper and lower quartiles must be from the upper and lower quartiles. 
            patch_artist=True,
            meanline=False, #the mean as a line
            showbox=True, #presented as a box
            showcaps=True, #two lines at the top and end
            notch=False 
            )
plt.title('the distribution of average exon lengths')
plt.show()
