from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playTestString
from Helpers.NoteRandomizer import randomizer


class KeyboardRobotlessDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Robotless Demo with Matching Rhythm and Notes"

    def start(self):
        self.announceStart()

        phrase = getManualInput()
        print(f"Recieved the following phrase: \n{phrase}")

        for i in range(len(phrase)):
            playTestString(phrase[i])
        
        print("randomizing...")
        randomizer(phrase)

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
