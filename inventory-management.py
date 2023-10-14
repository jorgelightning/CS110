#Lab 5 - Lists and Files
#Jorge 
import csv

def main():
    cont = 0

    infileR = open('inventory.csv', 'r')
    infileA = open('inventory.csv', 'a')

    while(cont != 'y'):

        print('\n')
        display_inventory(infileR)
        total_inventory_value()

        print('\n' + '1) Add a new item to the inventory')
        print('2) Delete a specific item from the inventory ')
        print('3) Update the price or quantity for an item in the inventory')
        choices = int(input('\n' + 'What is one of the three actions would you like to take: '))

        if choices == 1:
            print('Add a new item to the inventory')
            add_inventory(infileA)
        
        if choices == 2:
            del_inventory(finding_index)
            print('Delete a specific item from the inventory')
        if choices == 3: 
            print('Update the price or quantity for an item in the inventory')

        cont = input('\n'+'Would you like to continue? (y/n)')

def display_inventory(infileR):
    with infileR as file:
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

def add_inventory(infileA):
    userInput = input('\n'+'Please enter inventory to add seperated in commas (name,price,quantity)')
    with infileA as file:
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
    
    infileW = open('inventory.csv', 'w')
    with infileW as f:
        writer = csv.writer(f)
        writer.writerows(rows)

main()
