 # import mysql.connector

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
Database = [
    {
        "id": "UPI0001",
        "name": "Giscard",
        "course": "Software Engineering",
        "level": 2,
        "password": "123456789",
        "email": "Giscard@gmail.com"
    },
    {
        "id": "UPI0002",
        "name": "Atta",
        "course": "Software Engineering",
        "level": 2,
        "password": "1234567811",
        "email": "Atta@gmail.com"
    },
    {
        "id": "UPI0003",
        "name": "Jones",
        "course": "Software Engineering",
        "level": 2,
        "password": "1234567812",
        "email": "Jones@gmail.com"
    },
    {
        "id": "UPI0004",
        "name": "Boakye",
        "course": "Software Engineering",
        "level": 2,
        "password": "1234567813",
        "email": "Boakye@gmail.com"
    }
]


class SoftwareEngineers:
    # Properties
    __id = None
    __name = None
    __course = None
    __level = None
    __password = None
    __email = None

    # Constructor or Initializer
    def __init__(self, Id, Name, Course, Level, Pasword, Email):
        self.__id = Id
        self.__name = Name
        self.__course = Course
        self.__Level = Level
        self.__pasword = Pasword
        self.__email = Email

    # Setters and getters
    def setId(self, Id):
        self.__id = Id

    def getId(self):
        return self.__id

    def setName(self, Name):
        self.__name = Name

    def getName(self):
        return self.__name




# object = SoftwareEngineers(1,1,2,2,2,3)
#
# object.Looper(Database)


# userinput = input("User ID:")
for data in Database:
    # if data.__getitem__('id') == userinput:
        object = SoftwareEngineers(data.__getitem__('id'), data.__getitem__('name'), data.__getitem__('course'),
                                   data.__getitem__('level'), data.__getitem__('password'), data.__getitem__('email'))
        # print(object.getId())
        # print(object.getName())
        print(object.getId())
        # break

# # print(object.getFirstName())
# object = SoftwareEngineers(1, 2, 3, 4, 5, 6)
# object.setId(45)
# print(object.getId())

def QueryIsGood(query):

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="django"
    )
    mycursor = mydb.cursor()

    mycursor.execute(query)

    myresult = mycursor.fetchall()
    return myresult
print(QueryIsGood("select * from tabalename"))
for data in QueryIsGood("select * from tabalename"):
    print(data)
