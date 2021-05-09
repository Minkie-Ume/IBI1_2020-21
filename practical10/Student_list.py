student_list=[]
class Student (object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		attribute='name:'+self.x+'   '+'program:'+self.y
		print(attribute)

a=Student('Wang Zhouyue','BMS')

