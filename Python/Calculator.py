# Suppose you spend ​$22 every week on coffee and ​$120 per month on food. 
# Over the course of a​ year, do you spend more on coffee or​ food? 
# Assume that there are 52 weeks in a year.

#If you have to do any assignments
#Formulas for Math 107 Quantitative Reasoning
def absolute(num):
    if not(a > 0):
        return num * -1
    else:
        return num

def sqrt(root, num):
    return num ** 1/root

def circleCir(radius):
    return print(2 * radius,"pi")

def circleArea(radius):
    return print(radius ** 2,"pi")

def cynArea(radius, height):
    return print(2 * radius * height + 2 * radius ** 2,"pi")

def recArea(length, width, height):
    return length * width * height

#P = Principle Value    APR = Annual Percentage Rate (as a decimal)
#Y = Number of Years    A = Accumulated Balance after 'Y' years
def sInterest(P, APR, Y):
    return print("Simple Interest Formula:\nA =",P * APR * Y + P)

def comInterest(P, APR, Y, n):
    statement = input("What kind of Compound Interest: (Yearly, More than Yearly, Continuous)")

    if statement == "Yearly":
        n = 1
        return print("Compound Interest Formula (Yearly):\nA =",P * (1 + APR/n)**Y)
    elif statement == "More than Yearly":
        n = int(input("Enter number of compounding periods per year:\n"))
        return print("Compound Interest Formula (>Yearly):\nA =",P * (1 + APR/n)**Y)
    else:
        return print("Compound Interest Formula (Continuous):\nA = Working on it")

comInterest(100.50, 0.2, 5)



#def factorial(num):
#Pyramids, Spheres, Trapezoids, Other Irregular Shapes