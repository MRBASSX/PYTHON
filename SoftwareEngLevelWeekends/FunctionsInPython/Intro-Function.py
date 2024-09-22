# Function In Python
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


# def login(email, password):
#     for data in Database:
#         if data.__getitem__('email') == email and data.__getitem__('password') == password:
#             print('Name: ', data.__getitem__('name'))
#             print('Index: ', data.__getitem__('indexNo'))
#             print('Email: ', data.__getitem__('email'))
#             print('Password: ', data.__getitem__('password'))
#             print('Course: ', data.__getitem__('course'))
#             print('Level: ', data.__getitem__('level'))
#             return True
#             break
#
#
# email = input("Enter Your Email")
# password = input("Enter Your Password")
#
# if login(email, password):
#     print("Hello ", email)
# else:
#     print("Wrong Credential Try Again")


def Find(Index):
    for data in Database:
        if data.__getitem__('indexNo') == Index:
            print('Name: ', data.__getitem__('name'))
            print('Index: ', data.__getitem__('indexNo'))
            print('Email: ', data.__getitem__('email'))
            print('Password: ', data.__getitem__('password'))
            print('Course: ', data.__getitem__('course'))
            print('Level: ', data.__getitem__('level'))
            return True
            break


IndexNumber = input("Enter Your Index")


if Find(IndexNumber):
    print()
else:
    print("No Record Found")
