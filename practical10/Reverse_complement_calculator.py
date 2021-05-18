#create a dictionary
table = {'A':'T','T':'A','C':'G','G':'C','a':'t','t':'a','g':'c','c':'g'}
def reverse_gene(G1):#define a function to get reverse DNA sequence
	reverse_sequence=''
	for i in G1:
		a = i
		b = table[i]#get the reverse base
		reverse_sequence += b
	return reverse_sequence[::-1]#get the sequence reversely.

reverse_gene("ACTTTACGGAT")#G1 is the specified DNA sequence

