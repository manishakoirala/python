
class myclass :
	def __init__(self,name,age) :
		self.name = name
		self.age = age
	def myfunction(self):
		print("name is" + self.name)

p = myclass("manisha",20)
p.myfunction()

