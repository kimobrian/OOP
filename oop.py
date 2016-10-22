import abc
class BaseClass(object):
	#Abstraction
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def showInput(self):
		return

class ChildClass(BaseClass): #Inheriting from the parent class
	def __init__(self):
		self.inherit = 'Inherited Value'
	def showInput(self):
		print('Implementation for abstract method')
	def showInput(self, inputA): #Method Overloading
		print('Overloading of method showInput:'+inputA)
#Method Overriding amd inheritance
class GrandChildClass(ChildClass):
	def showInput(self,inputA):
		print('Overring parent class implementaion:'+inputA)
		print('Inherited attribute:'+self.inherit)
child = ChildClass()
child.showInput('Username, Brian')

grandChild = GrandChildClass()
grandChild.showInput('Different Implementation')

#Polymorphism
class Bear(object):
	def __init__(self):
		self.__priv='Private Member' #Encapsulation
	def sound(self):
		print("Groarrr")
 
class Dog(object):
	def sound(self):
		print("Woof woof!")
 
def makeSound(animalType):
	animalType.sound()
 
bearObj = Bear()
dogObj = Dog()
makeSound(bearObj)
makeSound(dogObj)
