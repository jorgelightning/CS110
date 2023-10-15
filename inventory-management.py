import csv

def main():
    cont = 0
    while(cont != 'n'):

        print('\n')
        display_inventory()
        total_inventory_value()

        print('\n' + '1) Add a new item to the inventory')
        print('2) Delete a specific item from the inventory ')
        print('3) Update the price or quantity for an item in the inventory')
        while True:
            try:
                choices = int(input('\n' + 'What is one of the three actions would you like to take (1,2,3): '))
                break
            except ValueError:
                print('\n'+'***WHOA! That\'s not a valid number! TRY AGAIN***')

        if choices == 1:
            add_inventory()
            print('**Added inventory**')
        if choices == 2:
            del_inventory(finding_index)
            print('**The item has been deleted**')
        if choices == 3: 
            print('Update the price or quantity for an item in the inventory')
            update_inventory(finding_index)

        cont = input('\n'+'Would you like to continue? (y/n): ')

#open inventory.csv and split by commas(,) and removed newline (\n) and formatted to clean nicely 
def display_inventory():
    with open('inventory.csv', 'r') as file:
        for line in file:
            words = line.split(',')
            display_text = str('{:<15}  {:<15}  {:<15}'.format(*words))
            display_text = display_text.strip()
            print(display_text)

#Goes through each list (name,price,quantity), multiple price(index[1])*quantity(index[2]), to get sum total 
def total_inventory_value():
    sumPrice = 0
    sumQuantity = 0
    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows = rows[1:]
        for i in rows:
            sumPrice += float(i[1]) * float(i[2])
            sumQuantity += float(i[2])

        print('\n'+'Price total:',sumPrice)
        print('Quantity total:', sumQuantity)

#Ask user to input csv friendly input then appends to newline 
def add_inventory():
    userInput = input('\n'+'Please enter inventory to add seperated in commas (name,price,quantity): ')
    with open('inventory.csv', 'a') as file:
            newLine = ''.join(userInput) + '\n'
            file.write(newLine)

#search through the nested list and used .index to return index location of the string 
def finding_index(selectedList,searchStr):
    for nestedlist in selectedList:
        if searchStr in nestedlist:
            return (selectedList.index(nestedlist))

#ask user for a string, used finding_index function to get index location, then delete 
#list at returned index, write changes in .csv file
def del_inventory(finding_index):
    userInput = str(input('\n'+'Please enter an ITEM NAME to delete: '))

    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    userInput_indexLocation = int(finding_index(rows,userInput))

    print(rows[userInput_indexLocation])
    del rows[userInput_indexLocation]
    
    with open('inventory.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

#ask user for a string, used finding_index function to get index location of the nested list,
#then ask user to update price(index[1]) or quanity(index[2] of the list (name,price,quantity),
#write changes in .csv file
def update_inventory(finding_index):
    userInput = str(input('\n'+'Please enter a ITEM to edit: '))

    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    userInput_indexLocation = int(finding_index(rows,userInput))

    print(rows[userInput_indexLocation])
    userInputUpdate = str(input('\n'+'Please enter PRICE or QUANTITY to update: ')).lower()
    if userInputUpdate == 'price':
        updatePrice = float(input('Please enter a new price: '))
        rows[userInput_indexLocation][1] = f'{updatePrice:.2f}'
        writePrice = str(rows[userInput_indexLocation])
        print(writePrice)

    if userInputUpdate == 'quantity':
        updateQuantity = int(input('Please enter a new positive integer quantity: '))
        rows[userInput_indexLocation][2] = updateQuantity
        writeQuantity = str(rows[userInput_indexLocation])
        print(writeQuantity)

    with open('inventory.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

main()
