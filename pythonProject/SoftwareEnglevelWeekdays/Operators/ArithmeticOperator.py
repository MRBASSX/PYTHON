# + , -, * ,/ , % , **

# A program that add, subtract, divide and  multiply

First_Number = float(input("Input First Number "))
op = input("Input Operator + - * /")
Second_Number = float(input("Input Second Number "))

if op == '+':
    print("The Sum of ", First_Number, " + ", Second_Number, " == ", First_Number + Second_Number)
elif op == '-':
    print("The Subtraction of ", First_Number, " - ", Second_Number, " == ", First_Number - Second_Number)
elif op == '*':
    print("The Product of ", First_Number, " * ", Second_Number, " == ", First_Number * Second_Number)
elif op == '/':
    print("The Division of ", First_Number, " / ", Second_Number, " == ", First_Number / Second_Number)

# print(First_Number - Second_Number)
# print(First_Number * Second_Number)
# print(First_Number / Second_Number)

# A program to check if A number is an Even or Odd Number

user = float(input("Enter a Number"))

even = user % 2

print(even)
