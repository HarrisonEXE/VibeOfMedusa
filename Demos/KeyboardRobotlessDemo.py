from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playTestString


# -- Class Description ------------------ #
# Manual keyboard input and text output   #
# --------------------------------------- #
class KeyboardRobotlessDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Robotless Demo"

    def start(self):
        self.announceStart()
        notes = getManualInput()
        # print(notes)
        for note in notes:
            playTestString(note.degree)

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
