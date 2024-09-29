
def EvenOrOdd(number):
    return number % 2 == 0


number = float(input("Input A Number"))
if EvenOrOdd(number):
    print(number," is an even number")
else:
    print(number," is an odd number")
