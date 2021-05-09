table={'A':'T','T':'A','C':'G','G':'C','a'='t','t'='a','c'='g','g'='c'}#create a dictionary
G1="ACTTTACGGAT"#G1 is the specified DNA sequence
G2=""#use to demonstrate the reverse DNA sequence
def reverse_gene(G1):#define a function to get reverse DNA sequence
	a = G1[i-1]
	b = table[a]
	G2 = G2+b

print(G2)

