compare = 6 <= 5  # (2 < 5) or (2 == 5)

compare = 6 >= 5  # (2 > 5) or (2 == 5)

compare = 5 < 5  # (2 < 5)

compare = 6 > 5  # (2 > 5)

compare = 5 != 5  # (2 != 5)

if compare:
    print(compare)
else:
    print(compare)

# Write a program to check
# which number is the largest among three Input Numbers


FirstNumber = float(input("Input First Number"))
SecondNumber = float(input("Input Second Number"))
ThirdNumber = float(input("Input Third Number"))

IsFirstLargest = FirstNumber > SecondNumber and FirstNumber > ThirdNumber
IsSecondLargest = SecondNumber > FirstNumber and SecondNumber > ThirdNumber
IsThirdLargest = ThirdNumber > SecondNumber and ThirdNumber > FirstNumber

# IsFirstLargest = (100 > 50) and (100 > 900)
# IsSecondLargest = (50 > 100) and (50 > 900)
# IsThirdLargest = (900 > 50) and (900 > 100)

print("First  is Largest", IsFirstLargest)
print("Second  is Largest", IsSecondLargest)
print("Third  is Largest", IsThirdLargest)
