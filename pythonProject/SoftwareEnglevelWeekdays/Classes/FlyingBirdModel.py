class FlyingBird:
    __left_wing = None
    __right_wing = None
    __left_leg = None
    __right_leg = None

    def __init__(self, LeftLeg, RightLeg, LeftWing, RightWing):
        self.__right_leg = RightLeg
        self.__left_leg = LeftLeg
        self.__left_wing = LeftWing
        self.__right_wing = RightWing

    def getLeftLeg(self):
        return self.__left_leg

    def getRightLeg(self):
        return self.__right_leg

    def getLeftWing(self):
        return self.__left_wing

    def getRightWing(self):
        return self.__right_wing

    def Fly(self, rightleg, leftleg, low, high, delay, rightwing, leftwing):
        print("Set getRightLeg  Pin to ", rightleg, high)
        print("Set getLeftLeg  Pin to ", leftleg, high)
        print("Delay.... ", delay)
        print("Set getRightLeg  Pin to ", low)
        print("Set getLeftLeg  Pin to  ", low)
        print("Delay.... ", delay)
        print("Set getLeftWing  Pin to ", rightwing, high)
        print("Set getLeftWing  Pin to ", leftwing, high)
        print("Delay.... ", delay)
        print("Set getLeftWing  Pin to  ", low)
        print("Set getLeftWing  Pin to  ", low)

    def Walk(self,rightleg, leftleg, low, high, delay):
        print("Set getRightLeg  Pin to ", rightleg, high)
        print("Set getLeftLeg  Pin to ", leftleg, high)
        print("Delay.... ", delay)
        print("Set getRightLeg  Pin to ", low)
        print("Set getLeftLeg  Pin to  ", low)
        print("Delay.... ", delay)
