#
#

def readFile():
    inputFile = open('Alice-in-Wonderland.txt', 'r')
    readFile = str(inputFile.read())
    return readFile

def main():
    frequency = {}
    alice = readFile().lower()
    aliceWord = alice.split()

    for word in aliceWord:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1
    inputSearch = str(input('what word are you looking for?: ')).lower()
    if(inputSearch not in frequency):
        print("## ERROR ## - The word you are looking for does not exist")
    else:
        print(f'The word \'{inputSearch}\' occurrance:',frequency[inputSearch])

main()