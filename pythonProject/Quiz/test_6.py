def Voter(age):
    return age >= 18


age = int(input("Input An Age"))

if Voter(age):

    print("You Can vote")
else:
    print("You CanT vote go Home")
