#reading and opening files 
fileRead = open('test.txt','r')
fileWrite = open('search_output.txt', 'w')
counter = 0

userInput = str(input('Please input key word to search: '))
print('')

for line in fileRead:
	line = line.rstrip('\n')
	wordFind = line.lower().find(userInput)
	print(line)
	if wordFind > -1:
		counter += 1
print('')
result_output = str(f'The word {userInput} was found on {counter} lines in the input file.')
print(result_output)
fileWrite.write(result_output)	
