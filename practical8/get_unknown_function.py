import os
import re
os.chdir("/Users/minkie/IBI1_2020-21/practical8")
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
gene = file.readlines()
output = []
content=''
for i in range (len(gene)):
        if gene[i].startswith(">") and re.search(r'unknown function',gene[i]):
                name = re.findall(r'^>.+?_',gene[i])
                output.append(name)
                a =''
                for n in range (len(gene[i:-1])):
                        if gene[i+n+1].startswith('>'):
                                break
                        else:
                                a=a+gene[i+n+1][:-1]
                content='             '+ str(len(a)) + '\n'
                output.append(content)

fout=open('unknown_function.fa',"w")
fout.write(" ".join('%s' %a for a in output))
fout.close()
		
		
