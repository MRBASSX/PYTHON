# IF STATEMENT

# 1. IF

i = 100
if False:
    print("True")

# 2. IF..ELSE

if i:
    print("True")
else:
    print("False")

# 3. IF..ELIF..ELSE

if (1 == 1 or 2 == 3) and 4 == 4:
    if 1 == 2:
        print("first Passport")
    else:
        print("Document Validation Fail")
elif False:
    print("Second GhanaCard")
elif False:
    print("Third VotersID")
else:
    print("Not Valid Document")

names = ["Shadrack", "Joseph", "Jonathan", "Jona"]

WhatsYourName = str(input("WhatsYourName"))

if WhatsYourName == names[0]:
    print("Welcome ", names[0])
elif WhatsYourName == names[1]:
    print("Welcome ", names[1])
elif WhatsYourName == names[2]:
    print("Welcome ", names[2])
elif WhatsYourName == names[3]:
    print("Welcome ", names[3])
else:
    print("No Record Found")
