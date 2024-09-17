# Function In Python

def login(Username, Password):
    if Username == "MrAbas" and Password == "123456789":
        return True
    else:
        return False


Username = float(input("Input First Number"))
Password = float(input("Input Second Number"))

print(login(Username, Password))
