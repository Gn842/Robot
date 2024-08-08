class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


    def moveForward(self):
        self.x += 1
        self.y += 1


    def moveBackwards(self):
        self.x -= 1
        self.y -= 1
    
    def print(self):
        print(self.x)
        print(self.y)
    
dhsRobot = Robot("Tiger", 0, 0)
fmhsRobot = Robot("Green", 0, 0)

dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
dhsRobot.moveForward()
fmhsRobot.moveBackwards()

dhsRobot.print()
fmhsRobot.print()
