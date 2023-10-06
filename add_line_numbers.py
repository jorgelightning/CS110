#Lab 4 - Files and Functions    
#Part 1 - Add Line Numbers 


def main():
	fileName = input('Please enter the name of the file including the extension: ')
	fileOpen = open(str(fileName),"r")
	
	#print(fileOpen.read())
	print('')
	
	line_processor(fileOpen)

def line_processor(fileOpen):
	line_number = 1
	for line in fileOpen:
		line = line.strip()
		print(f"{line_number}: {line}")
		line_number += 1 

main()
