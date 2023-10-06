#Lab 4 - Files and Functions    
#Part 1 - Add Line Numbers 


def main():
	line_number = 1 
	fileName = input('Please enter the name of the file including the extension: ')
	fileOpen = open(str(fileName),"r")
	
	#print(fileOpen.read())
	print('')
	for line in fileOpen:
		line = line.strip()
		print(f"{line_number}: {line}")
		line_number += 1


main()
