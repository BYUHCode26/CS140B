#Assignment 1
print("Assignment 1")

#Given Variables
qtyPurchased = 3
unitPrice = 8.00
taxRate = 0.05
#Variables for the subtotal, total, and tax (Can find out these variables with any value.)
tax = (round(unitPrice * qtyPurchased * taxRate * 100))/100
subtotal = unitPrice * qtyPurchased
total = unitPrice * qtyPurchased + tax
#Print the required answers
print("Tax:",tax)
print("Subtotal:",subtotal)
print("Total:",total)

print("")
print("Assignment 2")

#Assignment 2
#Given Variables
a = 8
b = 3
c = 2
#Total and print
total2 = (a + b) * c
print("Total:",total2)

print("")
print("Assignment 3")

#Assignment 3
#Syntax Error (You have to add the parenthesses after the "print" function)
number = 15.3
print(number)

print("")
print("Assignment 4")

#Assignment 4
#Given Variables
quiz1 = 86
quiz2 = 90
quiz3 = 88
#Figure out average, and print
avgQuizScore = (quiz1 + quiz2 + quiz3)/3
print("The average quiz score is:",avgQuizScore)

print("")
print("Assignment 5")

#Assignment 5
#Ask the user to input minutes, and then print into a clock format
min = int(input("How many minutes have elapsed?"))
hours = int(min/60)
minNew = min % 60
print(hours,":",minNew)