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
        choices = int(input('\n' + 'What is one of the three actions would you like to take: '))

        if choices == 1:
            print('Add a new item to the inventory')
            add_inventory()
        
        if choices == 2:
            del_inventory(finding_index)
            print('**The item has been deleted**')
        if choices == 3: 
            print('Update the price or quantity for an item in the inventory')
            update_inventory(finding_index)

        cont = input('\n'+'Would you like to continue? (y/n)')

def display_inventory():
    with open('inventory.csv', 'r') as file:
        for line in file:
            words = line.split(',')
            display_text = str('{:<15}  {:<15}  {:<15}'.format(*words))
            display_text = display_text.strip()
            print(display_text)

def total_inventory_value():
    sumPrice = 0
    sumQuantity = 0
    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows = rows[1:]
        for i in rows:
            sumPrice += float(i[1])
            sumQuantity += float(i[2])

        print('\n'+'Price total:',sumPrice)
        print('Quantity total:', sumQuantity)

def add_inventory():
    userInput = input('\n'+'Please enter inventory to add seperated in commas (name,price,quantity)')
    with open('inventory.csv', 'a') as file:
            newLine = ''.join(userInput) + '\n'
            file.write(newLine)

def finding_index(selectedList,searchStr):
    for nestedlist in selectedList:
        if searchStr in nestedlist:
            return (selectedList.index(nestedlist))

def del_inventory(finding_index):
    userInput = str(input('\n'+'Please enter a product name is delete: '))

    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    userInput_indexLocation = int(finding_index(rows,userInput))

    del rows[userInput_indexLocation]
    
    with open('inventory.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def update_inventory(finding_index):
    userInput = str(input('\n'+'Please enter a product to edit: '))

    with open('inventory.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    userInput_indexLocation = int(finding_index(rows,userInput))

    print(rows[userInput_indexLocation])
    userInputUpdate = str(input('\n'+'Price or Quantity did you want to update? ')).lower()
    if userInputUpdate == 'price':
        updatePrice = float(input('What would you like to the price to be? '))
        rows[userInput_indexLocation][1] = updatePrice
        writePrice = str(rows[userInput_indexLocation])
        print(writePrice)

    if userInputUpdate == 'quantity':
        updateQuantity = str(input('What would you like to the quantity to be? '))
        rows[userInput_indexLocation][2] = updateQuantity
        writeQuantity = str(rows[userInput_indexLocation])
        print(writeQuantity)

    with open('inventory.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

main()
