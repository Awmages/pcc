#IF statement

#if something is true do something
#indentions are SUPER important!!

#if statement
x = 9
y = 1

if x > y:
    print("x is larger than y")

if y > x:
    print("y is larger than x")


#if with elif statement
# backup if statement if the first isn't true

if x > 10:
    print ('x is larger than 10')
elif x == 9:
    print('x is equal to 9')
elif x == 2:
    print('X is equal to 2')

print("done")

#if with elif and else statement
# else says that if everything else above is false the run

inp = int(input("enter a number: "))
if inp == 1:
    print ('you entered 1, not very creative')
elif inp == 2:
    print ("you entered 2, that's 1 more than 1")
elif inp == 3:
    print ("you entered 3, that's a lotta numbers")
else:
    print("no idea what number you entered!!")

#If statements can have only 1 if 1 else, and as many elif as needed!!!
