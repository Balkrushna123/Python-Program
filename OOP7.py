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
		print(Demo.A)
		# print(Demo.B)

	def __del__(self):
		print("Inside Destructor")

def main():
	Demo.fun_static()

if __name__ == "__main__":
	main()