import os
import re
os.chdir("/Users/minkie/IBI1_2020-21/practical8")
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
#open the file fasta
gene = file.readlines()
output = []#set a new list to place the result
content=''
for i in range (len(gene)):
        if gene[i].startswith(">") and re.search(r'unknown function',gene[i]):
                name = re.search(r'^>.+?_',gene[i]).group()
                output.append(name)
                a =''
                for n in range (len(gene[i:-1])):#extract and calculate sequence
                        if gene[i+n+1].startswith('>'):
                                break
                        else:
                                a=a+gene[i+n+1][:-1]+'\n'
                content='             '+ str(len(a)-n) + '\n'+a+'\n'
                output.append(content)
#len(a)-n means calculate the number of sequence.Because in use '\n' to change lines in a , I need to minus n to get the right number, n = the number of "\n"


#set a new fasta
fout=open('unknown_function.fa',"w")
fout.write(" ".join('%s' %a for a in output))
fout.close()
		
