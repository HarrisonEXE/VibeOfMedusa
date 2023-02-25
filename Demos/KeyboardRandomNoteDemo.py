from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playString, setupRobots
from numpy.random import randint


class KeyboardRandomNoteDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Demo with Randomized Notes and Matching Rhythm"

    def start(self):
        self.announceStart()

        setupRobots()

        phrase = getManualInput()
        print(f"Recieved the following phrase: \n{phrase}")

        phrase.notes = self.getRandomizedNotes()
        print(f"Changed to the following phrase: \n{phrase}")

        for i in range(len(phrase)):
            playString(phrase[i])

    def getRandomizedNotes(self):
        return randint(1, 5, 5)

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
