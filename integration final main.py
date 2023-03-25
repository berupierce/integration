# Beru Pierce
# examples of each numeric operator.
# introduction to user
print("Hi there!")
nameUser=input("What is your name? ")
print(("Welcome ")+nameUser,"\n")
print("I am going to go over numeric operators.")
# addition
print("Lets do addition!")
# using int and input
number1=input("Enter a number: ")
num1=int(number1)
number2=input("Enter a second number: ")
num2=int(number2)
sum=num1+num2
print("Sum:",+sum,"\n")
# subtraction
print("We can also do subtraction!")
#combining int & input on the same line
num3=int(input("Enter a number: "))
num4=int(input("Enter a second number: "))
difference=num3-num4
print("Difference:",+difference,"\n")
# multiplication
multiply='Here is an example of multiplication. '
equation='56 times 78?'
# using sep to have variable assigned statements print on the same line
print(multiply,equation,sep='What is ')
print("56*78= ",56*78,"\n")
# exponents
print("Next there are exponents.")
print("What is the value of 4^2?")
print("4**2= ",4**2,)
print("\n")
# division
# floor division
# end to have print statements on the same line
print("Next there is division and floor division.",end=' ')
print("We will use 25/7 for this example.")
print("25/7= ",25/7)
print("Floor division works a little bit different.")
print("25//7= ",25//7,"\n")
# modulus
# using 25//7 to show connection between floor division and modulus
print("Finally, we will use 25//7 once again.",end=' ')
print("Modulus is the remainder of floor division and is represented by %.")
print("25%7= ",25%7)
print("\n")
# modulus explanation
print("Floor division and modulus go together. Floor division gave us 3, and modulus gave us 4.")
print("7 goes into 25 3 times with a remainder of 4. That is where modulus comes from.")
# stackoverflow.com
# end of sprint 1
# help from the think python book
#using a for loop to list numbers 1-50
print("\n")
print("Here is a list of numbers between 1 and 50:")
x=1
for x in range(1,51):
    print(x, end=", ")
    x += 1
print("\n")
#find the smallest and highest number
def lowerNum(num5,num6):
    if num5<num6:
        lower=num5
    elif num6<num5:
        lower=num6
    elif num5==num6:
        lower=num5 and num6
    return lower
def upperNum(num5,num6):
    if num5>num6:
        upper=num5
    elif num6>num5:
        upper=num6
    elif num5==num6:
        upper=num5 and num6
    return upper
def main():
    num5 = int(input("Now enter a number between 1-50: "))
    num6 = int(input("Now enter another number between 1-50: "))
    lowern = lowerNum(num5,num6)
    print("The smaller number is: ", lowern)
    uppern = upperNum(num5,num6)
    print("The higher number is: ", uppern,"\n")
main()
#find sum of numbers using while loop
print("We can use loops to find the sum of numbers. Enter 0 to end.")
total=0
numberEntered=int(input("Enter any number: "))
while numberEntered!=0:
    total+=numberEntered
    numberEntered=int(input("Enter any number: "))
print("Total= ",total,"\n")
#using not boolean operator
oddEven=int(input("Enter a number: "))
if not oddEven%2==0:
    print("Number is odd.")
else:
    print("Number is even.","\n")
input("Press any key to exit.")