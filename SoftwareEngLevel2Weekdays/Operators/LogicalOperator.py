
class logic():
    def logistic(self):
        # and , or , not

        # A program to Check If A person can Vote Or Not

        age = int(input("Input Your Age"))
        can_vote = age >= 18
        can_vote2 = age > 18 or age == 18

        if (can_vote or can_vote2) and (can_vote2 or can_vote):
            print("You can Vote")
        else:
            print("You cant Vote")

        # A Program to Check The largest Number Among Three

        First_Number = int(input("Enter First Number"))
        Second_Number = int(input("Enter Second Number"))
        Third_Number = int(input("Enter Third Number"))

        if First_Number > Second_Number and First_Number > Third_Number:
            print("First Number is Greatest")
        elif Second_Number > First_Number and Second_Number > Third_Number:
            print("Second Number is Greatest")

        elif Third_Number > First_Number and Third_Number > Second_Number:
            print("Third Number is Greatest")


