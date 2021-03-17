gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
L = sorted(gene_lengths)
L.sort()#sorted the list
print(L)
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure() #gives an plot region
ax = fig.add_subplot(111)
ax.boxplot(gene_lengths)#gives the boxplot
plt.show()
