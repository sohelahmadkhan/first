def add(a,b):
	sum = a + b
	return sum

def sub(a,b):
	sub = a - b
	return sub

while True:
	print " 1. Addition \n 2. Subtraction \n 3. Exit"
	n = int(raw_input('Enter your choice : '))
	
	if not n == 3: 
        	a = int(raw_input("enter value of A : "))
	    	b = int(raw_input("enter value of b : "))

	if n == 1:
		print  'Addition is :',add(a,b)
	elif n == 2:
		print 'Subtraction is : ', sub(a,b)
	else:
		break

print hello
print changes in remote location

