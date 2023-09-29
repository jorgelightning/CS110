#Part 3 - Shopping Cart w/ functions

def displayMenu():
	global total, g_total
	print("Welcome to the Healthy Fruits Shop!")
	raspberries = input("Please enter how many pounds of raspberries you would like to buy ($1.75 per pound): ")
	while raspberries.isdigit() != True:	
		raspberries = input("Please enter a valid input: ")
	raspberries = float(raspberries) * 1.75
	strawberries = input("Please enter how many pounds of strawberries you would like to buy ($1.25 per pound):" )
	while strawberries.isdigit() != True:	
		strawberries = input("Please enter a valid input: ")
	strawberries = float(strawberries) * 1.25
	apples = input("Please enter how many apples you would like to buy ($0.5 per apple): ")
	while apples.isdigit() != True:	
		apples = input("Please enter a valid input: ")
	apples = float(apples) * 0.50
	mangoes = input("Please enter how many mangoes you would like to buy ($1.75 per mango): ")
	while mangoes.isdigit() != True:	
		mangoes = input("Please enter a valid input: ")
	mangoes = float(mangoes) * 1.75

	total = raspberries + strawberries + apples + mangoes
	g_total = raspberries + strawberries + apples + mangoes

	#print("$""%.2f" % raspberries)
	#print("$""%.2f" % strawberries)
	#print("$""%.2f" % apples)
	#print("$""%.2f" % mangoes)
	print("The total is: $""%.2f" % total)

def getPayment():
	global total, customer_payment, g_total
	customer_payment = float(input("Please enter how much the customer will pay: "))
	total = customer_payment - total
	total = abs(total)
	if customer_payment < g_total:
		print("Please cover the rest of the cost: $""%.2f" % total)
		add_on_payment = float(input("Please enter new payment: "))
		total = add_on_payment - total

def calculateChange():
	if customer_payment > g_total or total >= 0:
		print("Thank you for your payment!")
		print("Here are the change to distribute to the customer")
		change = total 
		print("The change to the customer would be: $""%.2f"%change)
		if change >= 5.0:
			five_dollar = change // 5
			change = change - (five_dollar * 5) 
			print(int(five_dollar), "of $5 note")
		if change >= 1.0:
			one_dollar = change // 1.0
			change = change - (one_dollar * 1)
			print(int(one_dollar), "of $1 note")
		if change >= 0.25:
	                quarter = change // 0.25
	                change = change - (quarter * 0.25)
	                print(int(quarter), "of a quarter")
		if change >= 0.05:
			nickle = change // 0.05
			change = change - (nickle * 0.05)
			print(int(nickle), "of a nickle")
		if change >= 0.01:
			pennies = change // 0.01
			change = change - (pennies * 0.01)
			print(int(pennies), "of a penny")
	else:
		print("Have a nice day!")
def main():
	continues = 'y'
	while(continues != 'n'):
		displayMenu()
		getPayment()
		calculateChange()
		print('')
		continues = input("Do you want to continue? y/n: ")
	
main()




