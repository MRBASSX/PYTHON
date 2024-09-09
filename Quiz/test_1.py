Number = int(input("Please Enter A Number"))

Lastdigit = Number % 10

EvenNumber = Lastdigit % 2

if EvenNumber == 0:
    print(Lastdigit, " Is An Even Number")
else:
    print(Lastdigit, " Is An Odd Number")

# print("Is An Even Number if True ==>", EvenNumber==0)
