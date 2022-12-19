def outer():
	print("Inside outer function")

	def Inner():
		print("Inside Inner function")
	Inner()


def main():
	outer()

if __name__=="__main__":
	main()