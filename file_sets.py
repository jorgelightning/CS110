###

import sys

#reading both files, read and split string into a set 
#put two sets on their own variable and printing outputs
#then used | for union, & intersection, and ^ for systematic difference
#used the three operations between the two sets printed results 
def readFiles(file):
    fileSet= {}
    setFile = open(file, 'rt')

    listFile = setFile.read().split()
    fileSet = set(listFile)
    return fileSet

setOne = readFiles(sys.argv[1])
setTwo = readFiles(sys.argv[2])

print('The set that is in ',sys.argv[1],setOne)
print('The set that is in ',sys.argv[2],setTwo)

print('All words for the two files are union', setOne | setTwo)
print('All words for the two files are intersected', setOne & setTwo)
print('All words for the two files are difference', setOne ^ setTwo)


