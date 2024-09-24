def LargestNumber(first, second, third):
    if first > second and first > third:
        # print("First is largest")
        return "First is largest"
    elif second > first and second > third:
        # print("Second is largest")
        return "Second is largest"
    elif third > first and third > second:
        # print("Third is largest")
        return "Third is largest"
    else:
        print("Two Numbers Cant The Same")


first = float(input("Input First Number"))
second = float(input("Input Second Number"))
third = float(input("Input Third Number"))

print(LargestNumber(first, second, third))
