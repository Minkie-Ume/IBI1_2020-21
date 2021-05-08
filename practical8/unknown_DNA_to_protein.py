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
		b=a.rstrip('\n')
		condons=[]
		for i in range(0, len(b), 3):
			c=b[i:i+3]
			condons.append(c)
		table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

		d=''
		for x in range (len(condons)):
			m=condons[i]
			n=table[m]
			d=d+n
		sequence=d+"\n"
		output.append(sequence)

fout=open('new_file.fa',"w")
fout.write(" ".join('%s' %a for a in output))
fout.close()

