a = 270802
b = 190784
c = 100321
d = a - c
e = a - b
X = True
Y = False
z = (X and not Y) or (Y and not X)
w = X !=Y
print(d)
print(e)
print(z)
print(w)

#three way to compare d & e:
#the first way:compare directly
if d > e:
	print('d is larger than e')
else:
	print('d is smaller than e')

#the second way:
f=d-e
if f>0:
	print('d is larger than e')
else:
	print('d is smaller than e')
#the third way:
f=d/e
if f>1:
	print('d is larger than e')
else:
	print('d is equal to e')
