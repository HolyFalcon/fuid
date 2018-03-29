#Workspace (30 lines)


























#--------------------------------------------------------------------------------------------------------------------------------------------------
#Clear Function
import os
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Convert line of strings to numbers in an array
def filearray():
	filename = input("Enter filename and dir")
	f = open(filename, "r")
	line = f.readline()
	split = line.split()
	nums = []
	for i in split:
		nums.append(int(i))
#--------------------------------------------------------------------------------------------------------------------------------------------------
#FizzBuzz Function
def fzbz(x):
	for n in range(x):
		if n % 15 == 0:
			print("FizzBuzz")
		elif n % 5 == 0:
			print("Buzz")
		elif n % 3 == 0:
			print("Fizz")
		else:
			print(n)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Exponent Calculator
def nk(n, k):
	answer = 1
	for x in range(k):
		answer *= n
	print(answer)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Numerical Sort Methods
def maxs(items):
	for i in range(len(items) - 1):
		for n in range(len(items) - 1):
			if items[n] > items[n + 1]:
				temp = items[n]
				items[n] = items[n + 1]
				items[n + 1] = temp
def mins(items):
	for i in range(len(items) - 1):
		for n in range(len(items) - 1):
			if items[n] < items[n + 1]:
				temp = items[n]
				items[n] = items[n + 1]
				items[n + 1] = temp
def merge(items):
	#Base Case
	if len(items) < 2:
		return
	#Cut Deck in Half
	mid = int(len(items) / 2)
	left = []
	right = []
	for i in range(0, mid):
		left.append(items[i])
	for i in range (mid, len(items)):
		right.append(items[i])
	#Sort Halves
	merge(left)
	merge(right)
	#Zip Halves Together
	L = 0
	R = 0
	M = 0
	
	while L < len(left) and R < len(right):
		if left[L] < right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	#Copy left from left
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1
	#copy left from right
	while R < len(left):
		items[M] = right[R]
		R += 1
		M += 1
#Note: I have no idea if rmerge actually works
def rmerge(items):
	#Base Case
	if len(items) < 2:
		return
	#Cut Deck in Half
	mid = int(len(items) / 2)
	left = []
	right = []
	for i in range(0, mid):
		left.append(items[i])
	for i in range (mid, len(items)):
		right.append(items[i])
	#Sort Halves
	reverse_merge(left)
	reverse_merge(right)
	#Zip Halves Together
	L = 0
	R = 0
	M = 0
	
	while L < len(left) and R < len(right):
		if left[L] > right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	#Copy left from left
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1
	#copy left from right
	while R < len(left):
		items[M] = right[R]
		R += 1
		M += 1
def shuffle(items):
	from random import randint
	for i in range(len(items)):
		index = randint(i, len(items) - 1)
		temp = items[i]
		items[i] = items[index]
		items[index] = temp
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Prime Function (Standalone)
def prime():	
	n = int(input("Enter a number: "))

	isPrime = True

	for x in range(2, int((n / 2) + 1)):
		if n % x == 0:
			isPrime = False
			break

	if isPrime:
		print("The number is prime.")
	else:
		print("The number is not prime.")
#Prime Function (Check)

	isPrime = True

	for x in range(2, int((n / 2) + 1)):
		if n % x == 0:
			isPrime = False
			break

	if isPrime:
		primelist.append
#--------------------------------------------------------------------------------------------------------------------------------------------------
