#Calculate min_max 
def main():
    userInput = ''
    numbers = []
    while(userInput != '-1'):
        userInput = input('Please enter a numerical value <-1 will exit program>: ')
        numbers.append(userInput)       
    numbers.remove('-1')
    max_num = max(numbers)
    min_num = min(numbers)
    print('The max value is: ',max_num)
    print('The min value is: ',min_num)

main()