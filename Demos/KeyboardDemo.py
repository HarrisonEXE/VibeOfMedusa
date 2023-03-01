from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playString, setupRobots, startThreads, turnOnLive


class KeyboardDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Demo with Matching Rhythm and Notes"

    def start(self):
        self.announceStart()

        setupRobots()
        startThreads()
        turnOnLive()

        phrase = getManualInput()
        print(f"Recieved the following phrase: \n{phrase}")

        for i in range(len(phrase)):
            playString(phrase[i])

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
