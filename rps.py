#rock, paper, scissors 
import random

cc = '' 
uc = '' 

restart_game = 1

while(restart_game == 1):
	computer_choice = (random.randint(1,3))
	if computer_choice == 1:
		cc = 'rock' 
	if computer_choice == 2:
		cc = 'paper'
	if computer_choice == 3:
		cc = 'scissors'

	print("Welcome to the Rock, Paper, Scissors Game!")
	print("1= Rock, 2= Paper, 3 = Scissors")
	user_choice = input("Please choose Rock, Paper, Scissors (Numerical Value): ")

	while user_choice not in ['1','2','3']:
		user_choice = input("Please enter a valid choice (1,2,3): ")

	if user_choice == '1':
		uc = 'rock'
	if user_choice == '2':
		uc = 'paper'
	if user_choice == '3':
		uc = 'scissors'

	print("You have picked: ",uc)
	print("The computer chose: ",cc)

	if uc == cc:
		print("its a tie") 
	elif uc=='rock' and cc=='scissors':
		print("##Rock beats scissors##")
	elif uc=='rock' and cc=='paper':
		print("Rock loses to paper")
	elif uc=='paper' and cc=='rock':
		print("##Paper beats rock##") 
	elif uc=='paper' and cc=='scissors':
        	print("Paper loses to scissors")
	elif uc=='scissors' and cc=='paper':
		print("##Scissors beat paper##")
	elif uc=='scissors' and cc=='rock':
		print("Scissors loses to rock")
	
	restart_game = input("Do you want to play again? Y/N: ")
	while restart_game not in ['Y','y','N','n']:
		restart_game = input("Please enter a valid input Y/y N/n: ")
	if restart_game in ['Y','y']: 
		restart_game = 1 
	if restart_game in ['N','n']:
		restart_game = 0
		
		 

