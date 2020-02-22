#!/usr/bin/env python3

#Changed shebang line to be correct. Was originally calling the shell.
#Reading data from the user's input

print("Hello, please enter an integer.\n")

while True:                                    #Added in while loops for the a and b variables.
    a = input("Enter a: ")                     #The "True" setting indicates that whenever the
    if (a.isdigit()):                          #input of a is an integer, the loop will break.
        break                                  #Otherwise the loops continues and badgers you
    else:                                      #for an integer.
        print("Please enter an integer.")

a = int(a)                                     #Converting the type of a to an int. Although
print("You entered", a, "which is a", type(a)) #we enter a number as the input, the type is
                                               #still considered a string.
while True:
    b = input("Enter b: ")
    if (b.isdigit()):
        break
    else:
        print("Please enter an integer.")

b= int(b)
print("You entered", b, "which is a", type(b))


#######################################################################
# HINT: why would we be checking what type a and b are again?
#       Let's assume we want a and b to be integers at this point
#######################################################################

print("What is", a, "now?", type(a))
print("What is", b, "now?", type(a))


total = a + b
print("a + b =", total, ", which is a", type(total))

difference = a - b
print("a - b =", difference, ", which is a", type(difference))

product = a * b
print("a * b =", product, ", which is a", type(product))

quotient = a / b
print("a / b =", quotient, ", which is a", type(quotient))

floor_quotient = a // b
print("a // b =",
        floor_quotient,
        ", which is a",
        type(floor_quotient),
        )

remainder = a % b
print("a % b =", remainder, ", which is a", type(remainder))

power = a ** b
print("a ** b =", power, ", which is a", type(power))

a += 1
print("Incrementing \"a\" by one results in", a, "which is a", type(a))

b -= 1
print("Decrementing \"b\" by one results in", b, "which is a", type(b))

a += 1.0
print("Incrementing \"a\" by 1.0 results in", a, "which is a", type(a))


print("Now \"a\" equals", a, "and is a", type(a))
print("Now \"b\" equals", b, "and is a", type(b))


total = a + b
print("a + b =", total, ", which is a", type(total))

difference = a - b
print("a - b =", difference, ", which is a", type(difference))

product = a * b #Changed indent. Was indented too much.
print("a * b =", product, ", which is a", type(product))

quotient = a / b
print("a / b =", quotient, ", which is a", type(quotient))

floor_quotient = a // b
print("a // b =", floor_quotient, ", which is a", type(floor_quotient))

remainder = a % b
print("a % b =", remainder, ", which is a", type(remainder)) #Switched comma to inside first "",
                                                             #added another after remainder, and
                                                             #another after a".

power = a ** b
print("a ** b =",
        power,
        ", which is a",
        type(power),
        )

a += 1
print("Incrementing \"a\" by one results in", a, "which is a", type(a))

print("Woohoo! Nicely done!")
