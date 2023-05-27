#IF statements

#if something is True do something
# indentions are SUPER!!! important!!!

#if statement
x = 2
y = 1

if x > y:
    print("x is > than y")

if y > x:
    print("y is > than x")

alexCity = "Andover"
calebCity = "countryside"
countrySide = "countryside"

if alexCity == calebCity:
    print("they must be neighbors")

if calebCity == countrySide:
    print("Caleb lives in the middle of nowhere")
    print("He must live in OK!!")
print("out of if statement")

value = 10

#if elif statements (else if)

if value == 1:
    print("value is 1")
elif value == 2:
    print("value is 2")
elif value == 3:
    print ("value is 3")

#if, elif, else statement (else is a catchall if the check doesn't fit the other statement(s))

if value == 1:
    print("value is 1")
elif value == 2:
    print("value is 2")
elif value == 3:
    print ("value is 3")
else:
    print("no clue what value is bro")

#if statements will escape after the process after it catches the first true operation

if 15%3 == 0:
    print('Escape Clause starring Tim Allen')
elif 15%5 == 0:
    print('')