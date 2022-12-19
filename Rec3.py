def DisplayR(no):
	print(no)
	no=no+1
	DisplayR(no)

def main():
	DisplayR(0)

if __name__=="__main__":
	main()

	# get recursion limit
	# set recursion limit