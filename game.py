import random
r = random.randint(0, 100)
c = 5
while True:
	print ("secreat number :",r)
	a = int(input("Enter your choice numbers 5 times chance: "))
	if a > r :
		c = c-1
		if c==0:
			break
		print("your chance is : ",c)
		print("your choice high !")
	elif a < r :
		c =c-1
		if c ==0:
			break
		print("your chance is : ",c)
		print("your choice number low !")
	else:
		print("congragrletion")
		break
