#write four functions for the different operation 
def add(num1,num2):
	result = int(num1) + int(num2)
	return(result)
def sub(num1,num2):
	result = int(num1) - int(num2)
	return(result)
def mul(num1,num2):
	result = int(num1) * int(num2)
	return(result)
def div(num1,num2):
	result = int(num1) / int(num2)
	return(result)

def main():
	math_operation_choice = ''
	back_to_begin = 'y'
	while(back_to_begin == 'y'):
		print("Welcome to the Calculator Program!")
		num1 = int(input("Please enter variable 1: "))
		num2 = int(input("Please enter variable 2: "))

		math_operation_choice = input("Please enter a mathematical operation (+,-,*,/): ")
		while math_operation_choice not in ['+','-','*','/']:
			math_operation_choice = input("Error, please enter one of these math operation (+,-,*,/): ")
		if(math_operation_choice == '+'):
			print(add(num1,num2))
		if(math_operation_choice == '-'):
			print(sub(num1,num2))
		if(math_operation_choice == '*'):
			print(mul(num1,num2))
		if(math_operation_choice == '/'):
			print(div(num1,num2))
		back_to_begin = input("Please enter y to continue: ")
main() 
