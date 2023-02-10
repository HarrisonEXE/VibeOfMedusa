from Demos.IDemo import IDemo
from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import playTestString


# -- Class Description ------------------ #
# Manual keyboard input and text output
# --------------------------------------- #
class KeyboardRobotlessDemo(IDemo):
    def __init__(self) -> None:
        self.name = "Keyboard Robotless Demo"

    def start(self):
        self.announceStart()

        phrase = getManualInput()
        print(f"Recieved the following phrase: \n{phrase}")

        print(f"Aggregated onsets: \n {phrase.aggregated_onsents}")

        for i in range(len(phrase)):
            playTestString(phrase[i])

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
