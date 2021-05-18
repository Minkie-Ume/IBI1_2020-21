def grade(name,portfolio,poster,mcq):#collect the information including name and the grade of portfolio,poster,mcq.
	score= 0.4*portfolio+0.3*poster+0.3*mcq
	return name,score

#as an example, and print out the result with name and grade
a=grade('Wang Zhouyue',70,80,90)
name = a[0]
grade=a[1]
print('name:'+str(name)+'     '+'grade:'+str(grade))


