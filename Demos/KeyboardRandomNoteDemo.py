from Handlers.InputHandler import getManualInput
from Handlers.RobotHandler import (playString, setupRobots, startThreads,
                                   turnOnLive)
from Helpers.NoteRandomizer import beat_randomizer

from Demos.IDemo import IDemo


class KeyboardDemo(IDemo):

    def __init__(self) -> None:
        self.name = "Keyboard Demo with Matching Rhythm and Notes"

    def start(self):
        self.announceStart()

        setupRobots()
        print("robot setup complete")

        startThreads()
        print("threads started")

        turnOnLive()
        print("live mode activated")

        input_phrase = getManualInput()
        random_phrase = beat_randomizer(input_phrase)
        print(f"Received the following phrase: \n{random_phrase}")

        for i in range(len(random_phrase)):
            playString(random_phrase[i])

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True
