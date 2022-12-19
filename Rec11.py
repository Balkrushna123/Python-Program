i=0    # global variable
def fun():
	
	if(i < 5):
		print(i)
		i=i+1  # i++
		fun()  # Recursive call

def main():
	fun()
if __name__=="__main__":
	main()