A = input("President Password")
B = input("Vice Password")
C = input("Speaker Password")

AP = "A"
BP = "B"
CP = "C"

if A == AP and (B == BP or C == CP):
    print("The Safe Is Open")
elif B == BP and C == CP:
    print("The Safe Is Open")
else:
    print("The Safe Is Locked")
