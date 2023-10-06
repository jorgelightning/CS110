def main():
	fileName = input('Please enter the name of the file including the extension: ')
	fileOpen = open(str(fileName),"r")
	
	#Creating next line for output to be clean 
	print('')
	
	line_processor(fileOpen)

#This is my important function to iterate through the lines and append line numbers 
def line_processor(fileOpen):
	line_number = 1
	for line in fileOpen:
		line = line.strip()
		print(f"{line_number}: {line}")
		line_number += 1 

main()
