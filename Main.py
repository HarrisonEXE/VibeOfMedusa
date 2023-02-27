from Demos.KeyboardDemo import KeyboardDemo
from Demos.KeyboardRobotlessDemo import KeyboardRobotlessDemo
from Demos.KeyboardRandomNoteDemo import KeyboardRandomDemo
class MedusaDemo:
    def __init__(self):
        self.keyboard_demo = KeyboardDemo()
        self.keyboard_robotless_demo = KeyboardRobotlessDemo()
        self.keyboard_randombeat_demo = KeyboardRandomDemo()


        self.current_demo = self.keyboard_robotless_demo

    def run(self):
        self.current_demo.start()


if __name__ == '__main__':
    demo = MedusaDemo()
    demo.run()
