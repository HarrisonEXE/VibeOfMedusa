from Demos.KeyboardDemo import KeyboardDemo
from Demos.KeyboardRandomNoteDemo import KeyboardRandomNoteDemo
from Demos.KeyboardRobotlessDemo import KeyboardRobotlessDemo
from Demos.MicDemo import MicDemo
from Demos.RandomizedMicDemo import RandomizedMicDemo
from Demos.VoiceRecognizer import VoiceDemo
from Handlers.RobotHandler import startThreads, setupRobots


class MedusaDemo:
    def __init__(self):
        self.keyboard_demo = KeyboardDemo()
        self.keyboard_robotless_demo = KeyboardRobotlessDemo()
        self.keyboard_random_note_demo = KeyboardRandomNoteDemo()
        # self.mic_demo = MicDemo()
        # self.randomized_mic_demo = RandomizedMicDemo()
        self.voice_demo = VoiceDemo()

        # self.current_demo = self.keyboard_demo
        self.current_demo = self.voice_demo

    def run(self):
        # setupRobots()
        # startThreads()
        self.current_demo.start()


if __name__ == '__main__':
    demo = MedusaDemo()
    demo.run()
