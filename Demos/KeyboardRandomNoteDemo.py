from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playString, setupRobots


class KeyboardRandomNoteDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Demo with Randomized Notes and Matching Rhythm"

    def start(self):
        self.announceStart()

        setupRobots()

        phrase = getManualInput()
        print(f"Recieved the following phrase: \n{phrase}")

        phrase.onsets = [3, 3, 3, 3, 3]
        print(f"Changed to the following phrase: \n{phrase}")

        for i in range(len(phrase)):
            playString(phrase[i])

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
