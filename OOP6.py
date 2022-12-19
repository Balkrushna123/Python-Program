class Demo:

	A=10   # class Variable

	def __init__(self):
		print("Inside Constructor")
		self.B=20  # Instance Variable

	def fun_instance(self):  # instance method
		print("Inside instance method")
		print(self.B)
		print(self.A)
		print(Demo.A)  # this is the correct way to access class variable

	@classmethod
	def fun_class(cls):  # class method
		print("Inside class method")
		print(cls.A)
		print(Demo.A)
		# print(cls.B)

	@staticmethod
	def fun_static():  # static method
		print("Inside static method")

	def __del__(self):
		print("Inside Destructor")

def main():
	# obj = Demo()  # Object Creation
	# obj.fun_instance()
	Demo.fun_class()
	obj=None

if __name__ == "__main__":
	main()