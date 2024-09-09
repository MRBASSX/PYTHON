# Dic = {'key1': 'Giscard', 'key2': 'Jones', 'key3': 'Atta Kay'}
# Set = {"Giscard", 'Jones','Atta',122}
# Tuple = ("Giscard", 'Jones','Atta',122)
# List = ["Giscard", 'Jones','Atta',122]

# list = [
#     {
#
#
#     },
#     {
#
#     }
#
# ]

# Set = {"Giscard", 'Jones', 'Atta', 122}
#
# for i in Set:
#     list.append(i)
#
# i = 0
# while i < Set.__len__():
#     print(list[i])
#
#     i = i + 1
"""
ssss
"""

#  intial  i= 0
# i = 0
# while condition:
#     print(i, " I am Looping")
#
#     i = i + 1
#      Update


# intial  i= 0
list = ["Giscard", "Jones", "Atta", "Abass"]

i = 0
while i < list.__len__():
    print(list[i], " I am Looping")

    i = i + 1
    # Update

while True:
    print("Main Menu")
    print("1 . Start ")
    print("x . Exit ")
    name = input("Please Enter Option:")
    print("Hello ", name, " Welcome to our Channel")
    if (name == "1"):
        while True:
            name = input("Please What is Your Age ?")
            print("Hello ", name, " Welcome to our Channel")

            if name == "back":
                break
    if name == "x":
        break
