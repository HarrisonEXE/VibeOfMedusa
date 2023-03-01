from Demos.KeyboardDemo import KeyboardDemo
from Demos.KeyboardRandomNoteDemo import KeyboardRandomNoteDemo
from Demos.KeyboardRobotlessDemo import KeyboardRobotlessDemo
from Demos.MicDemo import MicDemo
from Handlers.RobotHandler import startThreads, setupRobots


class MedusaDemo:
    def __init__(self):
        self.keyboard_demo = KeyboardDemo()
        self.keyboard_robotless_demo = KeyboardRobotlessDemo()
        self.keyboard_random_note_demo = KeyboardRandomNoteDemo()
        self.mic_demo = MicDemo()

        # self.current_demo = self.keyboard_demo
        self.current_demo = self.mic_demo

    def run(self):
        # setupRobots()
        # startThreads()
        self.current_demo.start()


if __name__ == '__main__':
    demo = MedusaDemo()
    demo.run()
