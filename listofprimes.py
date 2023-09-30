#List of primes 

def list_primes(user_inputs):
	for i in range(1,user_inputs+1):
		if(i==2 or i==3 or i==5 or i==7):
			print(i, end=" ")
		if i % 3 != 0 and i % 2 != 0 and i % 5 != 0 and i % 7 != 0:
			print(i, end=" ")
def is_prime(i):
		print('')
		if(i==2 or i==3 or i==5 or i==7):
			return True
		if i % 3 != 0 and i % 2 != 0 and i % 5 != 0 and i % 7 != 0:
			return True
		else:
			return False


def main():
	user_inputs = int(input("Please input a positive numerical value: "))
	list_primes(user_inputs)
	prime = is_prime(user_inputs)
	print('Is the positive numerical value prime? ',prime)

main()





