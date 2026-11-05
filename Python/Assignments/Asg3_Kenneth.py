import math

print("Problem 1")
# Write a python function named computeHypotenuse that is passed two values representing the length 
# of the sides of a right triangle.  The functions should use the two lengths to compute and return the 
# hypotenuse of the triangle.  The formula for the hypotenuse of a right triangle is: 
# where c is the length of the hypotenuse and a and b are the lengths of the other two sides.  
# Reminder: to compute the square root of a number, raise the number to the 0.5 power.

# Use the following to test your function:
# print( computeHypotenuse(3, 4) )  # should be 5 (or something very close).
# print( computeHypotenuse(6, 8) )  # should be 10 (or something very close).

def computeHypotenuse(a,b):
    return (a**2 + b**2)**0.5
    
leg1 = int(input("Enter a number for leg 1: "))
leg2 = int(input("Enter a number for leg 2: "))
print(computeHypotenuse(leg1, leg2))


print("")
print("Problem 2")
# Write a python function named absolute, that is passed a number and returns the absolute value of that number.  
# (Note: there is a built-in python function named abs.  DO NOT USE IT.)  
# The function should use an "if" statement to test if the value is less than zero.  
# If it is, return -1 times the value, otherwise return the value.

# Use the following to test your function:
# print( absolute(-4.5) )     should be 4.5
# print( absolute(0) )          should be 0
# print( absolute(1) )          should be 1

def absolute(x):
    if (x < 0):
        x *= -1
    return x

i = float(input("Enter a number to make absolute: "))
print(absolute(i))

print("")
print("Problem 3")
# When a \n is placed in a python string, it tells python to go to a new line when printing.  
# For example, print("hello\nworld") would output:

# hello

# world

# Write a python function named repeatIt, that is passed a greeting and a number of times the 
# greeting is to be repeated.  The function should print the greeting the given number of times 
# with each being on a separate line.  Hint: concatenate the greeting with "\n" to print on a new 
# line each time.  This function should not return a value.
# Use the following to test your function:

# repeatIt("Hello", 2)         should print Hello twice on two different lines.
# repeatIt("Kumusta", 5)  should print Kumusta 5 times on different lines.

def repeatIt(Hello, r):
    return print((Hello + "\n") * r)

Greet = input("Input your greeting: ")
Repeat = int(input("How many times: "))
repeatIt(Greet, Repeat)