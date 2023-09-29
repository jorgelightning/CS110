#Expense Tracker
transportation_expense = 0
transportation_counter = 0
food_expense = 0
food_counter = 0
medical_expense = 0
medical_counter = 0
entertainment_expense = 0
entertainment_counter = 0

continues = 'y'

def categorize(expense, category):
	global transportation_expense,food_expense,medical_expense,entertainment_expense
	global transportation_counter, food_counter, medical_counter, entertainment_counter

	if category == 1:
		transportation_expense += expense
		transportation_counter += 1
		print(transportation_expense)
	if category == 2:
		food_expense += expense
		food_counter += 1
		print(food_expense)
	if category == 3:
		medical_expense += expense
		medical_counter += 1
		print(medical_expense)
	if category == 4:
		entertainment_expense += expense
		entertainment_counter += 1
		print(entertainment_expense)

def displayExpenseReport():
	global transportation_expense,food_expense,medical_expense,entertainment_expense
	global transportation_counter, food_counter, medical_counter, entertainment_counter
	print('')

	if transportation_expense == 0:
		print('There are no expenses in the transportation category!')
		print('')
	else:	
		print('Total transportation expense is: ',transportation_expense)
		print('Average transportation expense is: ',transportation_expense/transportation_counter)
		print('')
	if food_expense == 0:
		print('There are no expenses in the food category!')
		print('')
	else:
		print('Total food expense is: ',food_expense)
		print('Average food expense is: ',food_expense/food_counter)
		print('')
	if medical_expense == 0:
		print('There are no expenses in the medical category!')
		print('')
	else:
		print('Total medical expense is: ',medical_expense)
		print('Average medical expense is: ',medical_expense/medical_counter)
		print('')
	if entertainment_expense == 0:
		print("There are no expenses in the Entertainment category!")
		print('')
	else:
		print('Total entertainment expense is: ',entertainment_expense)
		print('Average entertainment expense is: ',entertainment_expense/entertainment_counter)
		print('')

def main():
	global continues
	print('Welcome to the Expense Tracker Program!')
	while(continues != 'n'):
		expense = int(input('Enter your expense: '))
		category = int(input('Enter a category - 1. Transportation, 2. Food, 3. Medical 4. Entertainment: '))
		categorize(expense, category)
		continues = input('Do you want to contnue? y/n: ')
	displayExpenseReport()

main() 
