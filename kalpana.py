number=int(input())
if number > 1:
	for i in range(2,number):
		if(number % i)==0:
			print(number,"no")
			break
	else:
		print(number,"yes")
