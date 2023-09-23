# Project 1  - Analyzing Text Files
# CS 110
# Jorge Portillo 

# Imports
import re # To use Regular Expressions
import sys # To access the input provided at the command line (command line parameters)

# Print the number of parameters / arguments provided by the user at the command line
print ("Number of arguments:", len(sys.argv), "arguments")

# Print the parameters printed at the command line
print ("Argument List:", str(sys.argv))

# The name of the text file is provided as the 2nd parameter and is accessed using index 1
# Index 0 contains the first element (name of the program)
# Index 1 contains the second element (name of the text file)
filename = sys.argv[1]

# Print the name of the text file to make sure that we're reading the correct text file
print(filename)

# Open the text file
file_handler = open(filename, "r") # The file is opened in READ mode using the "r" parameter

# Create empty lists
all_words = [] # This list will contain all the words in the text file
all_characters = [] # This list will contain all the characters in the text file

# Read the text file into the program one line at a time using a for loop
for one_line in file_handler:
    
    # Add all the characters in the file to the allcharacters list, one line at a time 
    all_characters.extend(one_line)

    # split the line with a regular expression on spaces
    # For example, "Hello, How are you?" is split into six strings: "Hello", ",", "How", "are", "you", "?"
    chunks = re.findall( r'\w+|[^\s\w]+', one_line)

    # If a line is empty, then do not add any words to the allwords list 
    if len(chunks) > 0:
        all_words.extend(chunks)

# This is to check that the contents of the file have been read into the all_characters and all_words lists
# For tiny_file.txt, len(all_characters) prints 20, len(all_words) prints 6
#print(len(all_characters))
#print(len(all_words))

# PART 1

# Initialize variables 
comma_counter = 0
vowel_counter_low = 0
consonant_counter_low = 0
vowel_counter_up = 0
consonant_counter_up = 0

#strings vowels and consonants string to look for 
vowels = "aeiouAEIOU"
consonants = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"
exit = 0

for consonants_char in all_characters:
	if(consonants_char.islower()):
		if consonants_char in consonants:
			consonant_counter_low += 1

for consonants_char in all_characters:
        if(consonants_char.isupper()):
                if consonants_char in consonants:
                        consonant_counter_up += 1

for vowels_char in all_characters:
	if(vowels_char.islower()):
		if vowels_char in vowels:
			vowel_counter_low += 1

for vowels_char in all_characters:
        if(vowels_char.isupper()):
                if vowels_char in vowels:
                        vowel_counter_up += 1

for character in all_characters:
	if(character == ","):
		comma_counter = comma_counter + 1
		
#	print(character)
total_low = vowel_counter_low + consonant_counter_low
total_up = vowel_counter_up + consonant_counter_up
total_vowel_low_up = vowel_counter_low + vowel_counter_up
print("The file contains",comma_counter, "commas.")
print("The file contains",vowel_counter_low, "lowercase vowels.")
print("The file contains",consonant_counter_low, "lowercase consonants.")
print("The file contains",vowel_counter_up, "uppercase vowels.")
print("The file contains",consonant_counter_up, "uppercase consonants.")
print(" ")
print("Totals: ")
print("The file contains",total_low, "lowercase vowels and consonants.")
print("The file contains",total_up, "uppercase vowels and  consonants.")
print("The file contains",total_vowel_low_up, "uppercase and lowercase vowels")
print(" ")

#PART 2 loop code for search query and exit when user type in "exit" (not case sensitive)
while(exit != 1):
	search_key_counter = 0
	search_key = input("Please enter a word to search: ") 
	sk_low = search_key.lower()

	for search_key_char in all_words:
		sk_char_low = search_key_char.lower()
		if sk_low in sk_char_low:
			search_key_counter += 1
	if(sk_low == 'exit' or sk_low == 'Exit'):
		exit = 1
		search_key = 'N/A'
		search_key_counter = 'N/A'
		print("Exiting and didn't find the word exit in the text")
		print(" ")


	print("The search key:",search_key, "was found",search_key_counter,"times in the text file:", filename)
	print(" ")


