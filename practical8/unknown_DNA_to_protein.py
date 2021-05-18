import os
import re
os.chdir("/Users/minkie/IBI1_2020-21/practical8")
file = open("unknown_function.fa")
gene = file.readlines()
output = []
content=''
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

for i in range (len(gene)):
	if gene[i].startswith('>'):
		output.append(gene[i].split(' ')[0]) # get the sequence
	else:
		sequence = gene[i].replace('\n', '') 
		condons=[]
		protein=''
		for e in range( 0,len(sequence),3):
			a=sequence[e:e+3]
			protein + = table[a]
		content="    "+str(len(protein))+ "\n"+protein+'\n'
		output.append(content)

fout=open('new_file.fa',"w")
fout.write(" ".join('%s' %a for a in output))
fout.close()

