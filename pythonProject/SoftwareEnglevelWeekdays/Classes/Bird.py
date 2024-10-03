from FlyingBirdModel import FlyingBird

Flying = FlyingBird(1, 2, 3, 4)

print(Flying.getLeftLeg())
Flying.Fly(Flying.getLeftLeg(), Flying.getRightLeg(), "LOW", "HIGH", 1000, Flying.getRightWing(), Flying.getLeftWing())

if (1 == "1"):
    Flying.Walk(Flying.getLeftLeg(), Flying.getRightLeg(), "LOW", "HIGH", 1000)
