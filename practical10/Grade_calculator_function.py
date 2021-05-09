class grade(object):
	def __init__(self,s,x,y,z):
		self.s=s
		self.x=x
		self.y=y
		self.z=z
		score= 0.4*x+0.3*y+0.3*z
		print(self.s+'    '+str(score))

a=grade('Wang Zhouyue',70,80,90)

