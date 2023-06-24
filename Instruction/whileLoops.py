##while loops execute if a condition is true

i=0
while i < 5:
    print(i)
    i = i+1

#break will stop the loop even if true
print("-----------------")

j = 1
while j < 5:
  print(j)
  if j == 3:
    break
  j += 1

#With the continue statement we can stop the current iteration, and continue with the next:
print("-----------------")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#With the else statement we can run a block of code once when the condition no longer is true:
print("-----------------")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")