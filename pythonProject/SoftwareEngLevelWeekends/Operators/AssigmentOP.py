# Assigment Operator
i = 0

i += 3  # i = i + 3
i += 4  # i = i + 4
i += 2  # i = i + 2
i %= 3  # i = i % 3
print(i)

# Write a program  to find the last digit of number
# and check if the number is even or Odd
number = float(input("Input a Number"))

lastdigit = number % 10

print(lastdigit)

Even = lastdigit % 2

IsEven = Even == 0

if IsEven:
    print(lastdigit, " Is Even")
else:
    print(lastdigit, " Is Odd")
