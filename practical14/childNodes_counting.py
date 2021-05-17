import re
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("/Users/minkie/IBI1_2020-21/practical14/go_obo.xml")
collection = DOMTree.documentElement
terms= collection.getElementsByTagName("term")
related_1=[]
for term in terms:
	defstr = term.getElementsByTagName('defstr')[0]
	if re.search(r'DNA',defstr.childNodes[0].data):
		id = term.getElementsByTagName('id')[0]
		related_1.append(id.childNodes[0].data)

n1=0			
for i in range (len(related_1)):
	a = related_1[i]
	print("related:"+related_1[i])
	for term in terms:
		is_a = term.getElementsByTagName('is_a')
		id_1=term.getElementsByTagName('id')[0]
		for x in range(len(is_a)):
			if is_a[x].childNodes[0].data==a:
				print(id_1.childNodes[0].data)
                        	n1 +=1
				a=id_1.childNodes[0].data

related_2=[]
for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        if re.search(r'RNA',defstr.childNodes[0].data):
                id = term.getElementsByTagName('id')[0]
                related_2.append(id.childNodes[0].data)

n2=0
for i in range (len(related_2)):
        a = related_2[i]
        for term in terms:
                is_a = term.getElementsByTagName('is_a')
                id_1=term.getElementsByTagName('id')[0]
                for x in range(len(is_a)):
                        if is_a[x].childNodes[0].data==a:
                                n2 +=1
                                a=id_1.childNodes[0].data

related_3=[]
for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        if re.search(r' protein ',defstr.childNodes[0].data):
                id = term.getElementsByTagName('id')[0]
                related_3.append(id.childNodes[0].data)

n3=0
for i in range (len(related_3)):
        a = related_3[i]
        for term in terms:
                is_a = term.getElementsByTagName('is_a')
                id_1=term.getElementsByTagName('id')[0]
                for x in range(len(is_a)):
                        if is_a[x].childNodes[0].data==a:
                                n3 +=1
                                a=id_1.childNodes[0].data
