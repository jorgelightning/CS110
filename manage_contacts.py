#
#

def readFileDictionary():
    contacts= {}
    contactsFile = open('contacts.txt', 'rt' ,encoding='utf-8')
    if(fileEmpty() == True):
        contacts = {}
    if(fileEmpty() == False):
        contactString = contactsFile.read()
        contacts = eval(contactString)
    return contacts

def fileEmpty():
    with open('contacts.txt', 'rt' ,encoding='utf-8') as contactsFile:
        line = contactsFile.read()

    if line == '':
        return True
    else:
        return False
    
def noExistFile(filename):
  try:
    with open(filename, "r") as f:
      pass
  except FileNotFoundError:
    with open(filename, "w") as f:
      pass

noExistFile('contacts.txt')
contacts = readFileDictionary()

def main():
    exit = 0
    while(exit != 1):
        while True:
            try:
                userAction = int(input('\nCONTACTS MANAGEMENT\n\n(1)Add a new entry\n(2)Change the phone number\n(3)Delete an entry\n(4)Display the contacts list\n(5)Exit the program\n\nWhat would you like to do: '))
                if not (1 <= userAction <= 5):
                    raise ValueError('Invalid number selection. Please enter number 1-5')
                break
            except ValueError:
                print('\n\n### Please enter a valid integer from the selection (1-5). TRY AGAIN... ##\n\n')

        if(userAction == 1):
            userName = str(input('What is the name would you like to add: ')).lower()
            userNumber = str(input('What is the number would you like to add: '))
            contacts[userName] = userNumber

        if(userAction == 2):
            findName = str(input('What is the contact name would you like to change: ')).lower()
            if findName in contacts:
                print('We have found the contact')
                findNumber = str(input('What number would you like to change to: '))
                contacts[findName] = findNumber

        if(userAction == 3):
            delName = str(input('What contact would you like to delete: ')) 
            del contacts[delName]

        if(userAction == 4):
            print('\nDisplaying the contacts')
            print('\n','{:<10} {:<10}'.format('NAME', 'PHONE'))

            for key, value in contacts.items():
                name = key
                phone = value
                print("{:<10} {:<10}".format(name, phone))

        if(userAction == 5):
            exit = 1
            contactsWrite = str(contacts)
            contactsFile = open('contacts.txt', 'w')
            contactsFile.write(contactsWrite)
            print('exit program')

main()