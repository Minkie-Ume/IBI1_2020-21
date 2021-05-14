import os
import re
os.chdir('/Users/minkie/IBI1_2020-21/practical11')
a=open('RandomSeq.fa')
b=open('SOC2_human.fa')
c=open('SOD2_mouse.fa')
randomseq=a.readlines()
human=b.readlines()
mouse=c.readlines()
aminoacid_1=''.join(re.findall(r'[A-Z]',randomseq[1]))
aminoacid_2=''.join(re.findall(r'[A-Z]',human[1]))
aminoacid_3=''.join(re.findall(r'[A-Z]',mouse[1]))                 
edit_distance_1 = 0
edit_distance_2 = 0
edit_distance_3 = 0
for i in range(len(aminoacid_1)):
        if aminoacid_1[i]!=aminoacid_2[i]:
                edit_distance_1 += 1

print (edit_distance_1)

for i in range(len(aminoacid_1)):
        if aminoacid_1[i]!=aminoacid_3[i]:
                edit_distance_2 += 1

print (edit_distance_2)
for i in range(len(aminoacid_2)):
        if aminoacid_2[i]!=aminoacid_3[i]:
                edit_distance_3 += 1

print (edit_distance_3)
