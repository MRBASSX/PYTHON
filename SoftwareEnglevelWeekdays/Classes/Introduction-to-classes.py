# class Personal_Information:
#     first_name = None
#     surname = None
#     middle_name = None
#     age = "aaaaa"
#
#     def __init__(self, FirstName, Surname, MiddleName,Age):
#         self.first_name = FirstName
#         self.surname = Surname
#         self.middle_name = MiddleName
#         self.age = Age
#
#     def __init__(self, MiddleName,Age):
#         self.middle_name = MiddleName
#         self.age = Age
#
#
#
# object = Personal_Information("First", "surname")

#
# print(object.first_name)


# class CanVoteOrNot:
#     def person(self, age):
#         return age >= 18
#
#     def Square(self, length):
#         return (2 * length)
#
#
# object = CanVoteOrNot()
# if object.person(18):
#     print("You can Vote")
# else:
#     print("You canT Vote")
#
# print(object.Square(20))

class SoftwareEngineers:
    # Properties
    first_name = None
    surname = None
    other = None
    height = None
    age = None

    # Constructor or Initializer
    def __init__(self, First_Name, Surname, Other, Height, Age):
        self.first_name = First_Name
        self.surname = Surname
        self.other = Other
        self.height = Height
        self.age = Age

    # Setters and getters
    def setFirstName(self, First_Name):
        self.first_name = First_Name

    def getFirstName(self):
        return self.first_name


object = SoftwareEngineers("A", "B", "C", "D", "E")

object.setFirstName("Mr Abass")

print(object.getFirstName())
