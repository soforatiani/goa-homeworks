def number():
	num=(int(input("enter number")))
	
	for i in range(num):

		if num%2==0:
			print(i)
			num=num+1
number()
