def Division(A,B):
	Ans=0.0
	Ans=A/B
	return Ans

def SmartDivision(Func_Name):
	def Inner(a,b):
		if a < b:
			a,b=b,a
		return Func_Name(a,b)

	return Inner

Division=SmartDivision(Division)

def main():
	No1=0
	No2=0

	No1=int(input("Enter first number: "))
	No2=int(input("Enter the secod number: "))

	ret=Division(No1,No2)

	print("Division is:",ret)

if __name__=="__main__":
	main()