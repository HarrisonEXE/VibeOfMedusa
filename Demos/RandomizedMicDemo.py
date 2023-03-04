import numpy as np
import pyaudio
from Demos.IMicDemo import IMicDemo

from Helpers.NoteRandomizer import beat_randomizer, basic_randomizer


# Purely for documentation purposes
def override(f):
    return f


class RandomizedMicDemo(IMicDemo):
    def __init__(self, sr=48000, frame_size=2400, activation_threshold=0.02, n_wait=16, is_lab_work=True):
        super().__init__(sr, frame_size, activation_threshold,
                         n_wait, is_lab_work)
        self.name = "Mic Demo with Randomized Beat"

    @override
    def alterPhrase(self, phrase):
        print("Randomizing beat...")
        random_phrase = beat_randomizer(phrase)
        return random_phrase
