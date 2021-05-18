class Student (object):
	def __init__(self,first_name,last_name,program):#collect the information
		self.first_name=first_name
		self.last_name=last_name
		self.program=program
		attribute='first name:'+self.first_name+'  last name:'+self.last_name+'   '+'  program:'+self.program
		print(attribute)#print out the information

#as an example
Student('Zhouyue','Wang','BMS')

