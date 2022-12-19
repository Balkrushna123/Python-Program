# multithreading
# ratri chi arati example(ekani sagala kam karane)

import os
import threading

def Fun(X):
	print("PID of Fun is:",os.getpid())
	print("PPID of Fun is:",os.getppid())
	print("Inside fun")
	for i in range(X):
		print("Fun:",i)

def Gun(X):
	print("PID of Gun is:",os.getpid())
	print("PPID of Gun:",os.getppid())
	print("Inside gun")
	for i in range(X):
		print("Gun:",i)

def main():
	No=5
	print("RID of parent process:",os.getpid())

	print("Thread name of main is:",threading.current_thread().name)

	thread1=threading.Thread(target=Fun,args=(No,),name='FunThread')
	thread2=threading.Thread(target=Gun,args=(No,),name='GunThread')
	
	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print("End of main")

if __name__=="__main__":
	main()