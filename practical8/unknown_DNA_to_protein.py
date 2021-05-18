import os
import re
os.chdir("/Users/minkie/IBI1_2020-21/practical8")
file = open("unknown_function.fa")
gene = file.readlines()#open and read file
output = []
content=''
#set a condons' dictionary
genetic_code = {'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U',
'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z',
'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K',
'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

for i in range (len(gene)):
	if gene[i].startswith('>'):
		output.append(gene[i].split(' ')[0]) # get the ID
	else:
		sequence = gene[i].replace('\n', '') #get the DNA sequence
		condons=[]
		protein=''
	for e in range( 0,len(sequence),3):#get the condon and amino acid
		a=sequence[i:i+3]
		condons.append(a)
	for x in range(len(condons)):
		protein + = genetic_code[condons[x]]
		content="    "+str(len(protein))+ "\n"+protein+'\n'
		output.append(content)

#set the new fasta file.
fout=open('new_file.fa',"w")
fout.write(" ".join('%s' %a for a in output))
fout.close()

