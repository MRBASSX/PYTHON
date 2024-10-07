from Traffic import Traffic
RedLight = "RedLight"
GreenLight = "GreenLight"
YellowLight = "YellowLight"
Object = Traffic(RedLight, GreenLight, YellowLight)
Object.TrafficLight(5, 0, 180, 1800000)
Object.TrafficLight(5, 0, 1800000, 1800)
Object.TrafficLight(5, 0, 18, 1800000)
Object.TrafficLight(5, 0, 180, 1800000)
Object.TrafficLight(5, 0, 1800000, 180)


