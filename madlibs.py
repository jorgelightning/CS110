#MadLibs game 
import random
outfile = open('madlib.txt', 'w')

personList = ['Ada Lovelace','Grace Hopper','Charles Babbage','Alan Turing']
placeList = ['Bishop','Joshua Tree','Lake Tahoe','Fontainebleau','Castle Rock','The Gunks']
adjectiveList = ['windy','lazy','calm','lively']
nounAList = ['hedgehogs','dogs','oranges','mangeos','bananas']
nounMList = ['chocolates','books','bow and arrows','climbing shoes','watches','surfboards','skateboards']

person = random.choice(personList)
place = random.choice(placeList)
adjective = random.choice(adjectiveList)
nounOne = random.choice(nounAList)
nounTwo = random.choice(nounMList)

lineOne = str(f'Last summer, we went for a vacation with {person} ')
lineTwo = str(f'on a trip to {place}. The weather there is very {adjective}! ')
lineThree = str(f'Northern {place} has many {nounOne}, and they make {nounTwo} there.')

#display to screen 
print(lineOne)
print(lineTwo)
print(lineThree)

#writing to file 
outfile.write(lineOne)
outfile.write(lineTwo)
outfile.write(lineThree)

