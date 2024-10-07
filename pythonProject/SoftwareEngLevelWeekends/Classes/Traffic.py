class Traffic:
    __RedLight = None
    __GreenLight = None
    __YellowLight = None

    def __init__(self, Red, Green, Yellow):
        self.__RedLight = Red
        self.__GreenLight = Green
        self.__YellowLight = Yellow

    def getRedLight(self):
        return self.__RedLight

    def getGreenLight(self):
        return self.__GreenLight

    def getYellowLight(self):
        return self.__YellowLight

    def TrafficLight(self, StateHigh, StateLow, TimeLow, TimeHigh):
        print(self.__RedLight, " is ", StateHigh, " for ", TimeHigh, "ms")
        print(self.__RedLight, " is ", StateLow, " for ", TimeLow, "ms")

        print(self.__GreenLight, " is ", StateHigh, " for ", TimeHigh, "ms")
        print(self.__GreenLight, " is ", StateLow, " for ", TimeLow, "ms")

        print(self.__YellowLight, " is ", StateHigh, " for ", TimeHigh, "ms")
        print(self.__YellowLight, " is ", StateLow, " for ", TimeLow, "ms")



