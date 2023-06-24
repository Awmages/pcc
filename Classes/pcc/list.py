#List stores multiple items in a single variable
# created using [] (square brackets)

# like a grocery list 
groceryList = ['bread', 'milk', 'eggs', 'juice','taco seasoning']
print(groceryList)

print('--------------------------')

gameLibrary= ['Doom', 'Halo', 'WoW', 'Lost Ark', 'Binding of Isaac']
#Q what value (index number) is Doom 0

#NEW FUNCTION TIME len(). len = length and gives the length of the list, tuple, dict, set, etc
print(len(gameLibrary))

print('--------------------------')

# list with [] attached with the index value inside will return the value located at that index
print(gameLibrary[2])

#going past the last index will error out
#print(gameLibrary[5])

print('--------------------------')

#using an index of -# will go backwards through the list. -1 is the very end, -2 is 1 before the end, etc
print(gameLibrary[-1])
print(gameLibrary[-2])


print('--------------------------')
# Slicing
# put a [] at the end of the list, and then a start and stop value seperated by : inside [1:4]. the program will list index 1, 2, 3 but not the ending (4).
print(gameLibrary[1:4])

print('----------Micks library----------------')
micksGameLibrary = gameLibrary[1:4]
print(micksGameLibrary)

print('--------------------------')
#append adds the item to the end of the list .append("stuff")
gameChart = ["Myth", "Full Metal Textris", "MLP attack of the Micks"]
gameChart.append("Python The Musical The Video Game")
gameChart.append(gameLibrary[2])
print(gameChart)


print('--------Delete---------------')
#Delete .remove("stuff")
#we want to remove myth from gameChart
gameChart.remove("Myth")
print(gameChart)

del gameLibrary[2]
print(gameLibrary)


#Q: Add Binding of isaac to micksGameLibrary & print . Should show ['Halo', 'WoW', 'Lost Ark', 'Binding Of Isaac']

print('--------List of Lists---------------')
#List-ception list inside list

#gameCompany=[        "EA",                           "Blizzard",                        "Ubisoft"]
gameCompany=[['Fifa', 'Madden', 'NHL 2023'], ['Diablo', 'SC2', 'WoW'], ['Assassin Creed', 'Division', 'Farcry']]
#Use 1 indexer we're going to get the whole list in that position
print(gameCompany[0])
#if we use 2 indexers we're going to get the game inside the company
print(gameCompany[0][2])

gameCompany=[[['Fifa 20', 'Fifa 21', 'Fifa 22', 'Fifa 23'], 'Madden', 'NHL 2023'], ['Diablo', 'SC2', 'WoW'], ['Assassin Creed', 'Division', 'Farcry']]

print(gameCompany[0][0][3])
