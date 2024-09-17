# Collections And Loops
Dic = {
    'indexNo': 'UY50001',
    'name': 'Shadrack',
    'level': 'Two',
    'course': " Engineering",
    'course': "Software Engineering",

}
Dic.__setitem__('course', "Software")

list = ["Shadrack", "Joseph", "Jonathan", "Jonathan"]
# list[0] = "Bro"
# list[3] = "Bro"

tuple = ("Shadrack", "Joseph", "Jonathan", "Jonathan")
# tuple[0] = "Bro"


set = {"Shadrack", "Joseph", "Jonathan", "Jonathan"}
set.remove("Shadrack")
listname = []

# for Data in Dic:
#     print(Dic.__getitem__(Data))
#     listname.append(Dic.__getitem__(Data))
#
# print(listname)



IndexNumber = input("Enter Student ID")
for Base in Database:
    if Base.__getitem__('indexNo') == IndexNumber:
        print("Name : ", Base.__getitem__('name'))
        print("IndexNo : ", Base.__getitem__('indexNo'))
        print("Level : ", Base.__getitem__('level'))
        print("Course : ", Base.__getitem__('course'))
        print("Password : ", Base.__getitem__('password'))
        print("Email : ", Base.__getitem__('Email'.lower()))
        print(" ")
        break

