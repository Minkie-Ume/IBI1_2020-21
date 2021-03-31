# What does this piece of code do?
# Answer: to get a random number n in range (1,50) from range (1,100)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	# get a random number n
	if n > 50:
		p = False
		#to get a loop, if n>50, return

print(n)