# While Loop

Database = [
    {
        'indexNo': 'UY50001',
        'name': 'Shadrack',
        'level': 'Two',
        'course': "Software Engineering",
        'password': 'qwerty360',
        'email': 'Shadrack@gmail.com'
    },
    {
        'indexNo': 'UY50002',
        'name': 'Jonathan',
        'level': 'Two',
        'course': "Software Engineering",
        'password': 'qwerty361',
        'email': 'Jonathan@gmail.com'
    },
    {
        'indexNo': 'UY50003',
        'name': 'Joseph',
        'level': 'Two',
        'course': "Software Engineering",
        'password': 'qwerty362',
        'email': 'Joseph@gmail.com'
    }
]

IndexNumber = input("Enter Student ID")

i = 0  # initial
while i < len(Database):  # condition
    if Database[i].__getitem__('indexNo') == IndexNumber:
        print("Name : ", Database[i].__getitem__('name'))
        print("IndexNo : ", Database[i].__getitem__('indexNo'))
        print("Level : ", Database[i].__getitem__('level'))
        print("Course : ", Database[i].__getitem__('course'))
        print("Password : ", Database[i].__getitem__('password'))
        print("Email : ", Database[i].__getitem__('Email'.lower()))
        print(" ")
        break  # Code Here
    i = i + 1  # Update
