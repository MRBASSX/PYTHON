class Personal_Information:
    first_name = None
    surname = None
    middle_name = None
    age = "aaaaa"

    def __init__(self, FirstName, Surname, MiddleName,Age):
        self.first_name = FirstName
        self.surname = Surname
        self.middle_name = MiddleName
        self.age = Age

    def __init__(self, MiddleName,Age):
        self.middle_name = MiddleName
        self.age = Age



object = Personal_Information("First", "surname")

print(object.first_name)
