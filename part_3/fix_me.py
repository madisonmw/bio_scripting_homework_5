#!/usr/bin/env python3

#Changed shebang line to be correct. Was originally calling the shell.
#Reading data from the user's input

print("Hello, please enter a number.\n")

#Added while loop with try/except added in. Although we really only need integers, I wanted to
#find out a way to make floats work, too. eval() evaluates what type of input is
#put in, so 2 is an int and 2.3 is a float, for example. While True is set, if type(a) is either a float
#or int, the loop stops. Any other input causes a NameError exception that prompts you for
#a number and continues the loop. I had to add the KeyboardInterrupt exception, since I could not ctrlC out of the
#script without it. I am not sure what raise does; however, the exception does not work
#without it.

while True:
    try:
        a = eval(input("Enter a: "))
        if type(a) == int or float:
            break
    except NameError:
        print("Please enter a number.")
    except KeyboardInterrupt:
        raise

print("You entered", a, "which is a", type(a))

while True:
    try:
        b = eval(input("Enter b: "))
        if type(b) == int or float:
            break
    except NameError:
        print("Please enter a number.")
    except KeyboardInterrupt:
        raise

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
