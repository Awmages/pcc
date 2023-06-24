##For loop is used to iterate over lists, tuples, sets, dicts, or strings

#For is a keyword

gameLibrary = ["Doom", "Halo","WoW", "Lost Ark", "Binding of Isaac", "Diablo 7"]

for x in gameLibrary:
    print(x)

print("-----------------")
#for in a string will print out each character
for x in "Oppenheimer":
  print(x)

print("-----------------")
#break will stop the loop before it completes

for x in gameLibrary:
  print(x)
  if x == "Diablo 7":
    break
  
#continue will stop current loop interation and start another
print("-----------------")
for x in gameLibrary:
  if x == "Halo":
    continue
  print(x)

