#List store multiple items in a single variable
# created using square brackets 

gameLibrary = ["Doom", "Halo","WoW", "Lost Ark", "Binding of Isaac"]
# allows duplicat items 
gameLibraryDup = ["Doom", "Halo","WoW", "Lost Ark", "DOom", "Binding of Isaac"]

#can call specific items by using print(groceryDup[2])
#how computers count (0,1,2,3,4,5,6,7,8,9,...)
# ["cat", "dog", "mouse", "horse", "narwhal"]
# 0 is cat 3 is horse

print(gameLibraryDup[2]) #shows the 3rd item

#slicining
print(gameLibraryDup[0:3]) #shows the first 4
print(gameLibraryDup[2:4]) #shows
print(gameLibraryDup[-1])

#apending a List
GameCart = ["Myth", "MLP attack of the Mick", "Full Metal Textris"]
GameCart.append("Python the Game")
print(GameCart)

#deleting from list
del GameCart[0]
print(GameCart)

##mini challenge use prompts to collect a user's input and add it to the gameChart list. then print the new list

#len() will tell us the length of list
print(len(GameCart))