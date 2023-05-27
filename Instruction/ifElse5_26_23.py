# If statements

# if something is true do something else
# indentions are SUPER important!!!


# if statement
x = 2
y = 1

if x > y:
    print("x is > than y")


# if with elif statement
# backup if statement if the first isn't true
inp = int(input("enter number: "))
if inp == 1:
    print("entered value is = to 1")
elif inp == 2:
    print('entered value is = 2')
elif inp == 3:
    print('entered value is = 3')

# if with else statement
# else says that if everything above is false then perform else

inp2 = int(input("enter number: "))
if inp2 == 1:
    print("entered value is = to 1")
elif inp2 == 2:
    print('entered value is = 2')
elif inp2 == 3:
    print ('entered value is = 3')
else:
    print('no idea what the entered value is')