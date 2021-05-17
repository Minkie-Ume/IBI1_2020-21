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

num=len(set(getall(dict,related_1)))#calculte the number of childnodes

