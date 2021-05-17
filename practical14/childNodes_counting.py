import re
from xml.dom.minidom import parse
import xml.dom.minidom
DOM = xml.dom.minidom.parse("/Users/minkie/IBI1_2020-21/practical14/go_obo.xml")
collection = DOM.documentElement
terms= collection.getElementsByTagName("term")
dict={}
#set a dictionary whose keys applying for <is_a>value and values applying for <id>values.
for term in terms:
        is_a = term.getElementsByTagName('is_a')
        id=term.getElementsByTagName('id')[0]
        for x in is_a:
            if not x.childNodes[0].data in dict:
                dict[x.childNodes[0].data] = [id.childNodes[0].data]#if x.childNodes[0].data isn't in the dictionary as a key,then set up a new key.
            else:
                dict[x.childNodes[0].data].append(id.childNodes[0].data)#if x.childNodes[0].data exits in the dictionary as a key, then append a new value for the key.

#select GO which is associated with DNA
related_1=[]
for term in terms:
	defstr = term.getElementsByTagName('defstr')[0]
	if re.search(r'DNA',defstr.childNodes[0].data):
		id = term.getElementsByTagName('id')[0]
		related_1.append(id.childNodes[0].data)

#set a function to collected the childnodes 
def getall(dict,lists):
    all = []
    for i in lists:
        if i in dict:
            childnode = dict[i]
            all += childnode
            all += getall(dict,childnode) 
    return all

num_DNA=len(set(getall(dict,related_1)))#calculte the number of childnodes

#the number of childNodes associated with ‘RNA’.
#select GO which is associated with RNA.
related_2=[]
for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        if re.search(r'RNA',defstr.childNodes[0].data):
                id = term.getElementsByTagName('id')[0]
                related_2.append(id.childNodes[0].data)

num_RNA=len(set(getall(dict,related_2)))

#the number of childNodes associated with ‘protein’.
#select GO which is associated with protein.
related_3=[]
for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        if re.search(r'Protein|protein',defstr.childNodes[0].data):
                id = term.getElementsByTagName('id')[0]
                related_3.append(id.childNodes[0].data)

num_protein=len(set(getall(dict,related_3)))
 
#the number of childNodes associated with ‘carbohydrate’.
#select GO which is associated with carbonhydrate.
related_4=[]
for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        if re.search(r'Carbohydrate|carbohydrate',defstr.childNodes[0].data):
                id = term.getElementsByTagName('id')[0]
                related_4.append(id.childNodes[0].data)

num_carbohydrate=len(set(getall(dict,related_4)))

#as a result:
#The number of childNodes of all DNA-associated terms is: 8651
#The number of childNodes of all RNA-associated terms is: 11004
#The number of childNodes of all protein-associated terms is: 33459
#The number of childNodes of all carbohydrate-associated terms is: 4879

#make a pie chart about these stastistics

from matplotlib import pyplot as plt
labels='DNA', 'RNA', 'protein','carbohydrate'
sizes=[num_DNA,num_RNA,num_protein,num_carbohydrate]
colors = ['c','m','g','b']
plt.pie(sizes,
       labels=labels,  
       autopct='%1.1f%%', 
       colors=colors,  
        startangle=90,  
        explode = [0.2,0,0,0],  
        shadow=False  
       )
plt.title('the proportion of childnodes for different molecule-associated terms')
plt.show()
 
