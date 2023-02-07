from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playString, setupRobots


# -- Class Description ------------------ #
# Manual keyboard input and robot output  #
# --------------------------------------- #
class KeyboardDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Demo"

    def start(self):
        self.announceStart()

        setupRobots()

        notes = getManualInput()
        # print(notes)
        for note in notes:
            playString(note.degree)

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
