a = 0
b = 1
i = 1
#define the initial value
while i in range(1,12):
	c = a + b
#get the number next to a and b
	a = b
	b = c
#get new a&b's value
	i = i + 1
#move on the code
print(c)
