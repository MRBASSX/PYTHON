class marker:
    __name = None
    __type = None
    color = None
    price = None
    image = None

    def __init__(self, Name,Type):
        self.__name = Name
        self.__type =Type

    def getName(self):
        return self.__name
    def getType(self):
        return self.__type


object = marker("Man","tempory")

print(object.getName())
print(object.getType())
