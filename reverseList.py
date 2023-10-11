#Reverse a list manually

#set of test lists
inputList1 = [1, 2, 3, 4]
inputList2 = ["Buzz", "Bing Bong", "Mr. Incredible", "Crush"]
inputList3 = [1.345, "CS110", 54, "is", 2130, "Awesome"]

#Loop on the length of the list and append reverse of the index to a new list 
def reverseList(inputList):
	listLength = len(inputList)
	newList = []
	for index in range(listLength):
		index = -abs(index+1)
		indexedValue = inputList[index]
		newList.append(indexedValue)
	return newList

#Printing the return list of the reverseList function 
def main():
	newList = reverseList(inputList1)
	print(f'The input list is {inputList1} \n and the reversed list is {newList}\n')
	newList = reverseList(inputList2)
	print(f'The input list is {inputList2} \n and the reversed list is {newList}\n')
	newList = reverseList(inputList3)
	print(f'The input list is {inputList3} \n and the reversed list is {newList}\n')

main()
