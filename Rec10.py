
def fun():
	i=0       #Local variable(Auto storage class)
	if(i < 5):
		print(i)
		i=i+1  # i++
		fun()  # Recursive call

def main():
	fun()
if __name__=="__main__":
	main()