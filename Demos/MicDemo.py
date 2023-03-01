import numpy as np
import pyaudio
import time

from threading import Thread, Lock, Event
from Classes.Phrase import Phrase
from Classes.audioDevice import AudioDevice
from Demos.IDemo import IDemo
from Handlers.RobotHandler import playString, playStringTemp
from Helpers.audioToMidi import AudioMidiConverter


class MicDemo(IDemo):
    def __init__(self, sr=48000, frame_size=2400, activation_threshold=0.02, n_wait=16):
        self.name = "Mic Demo with Matchnig Notes and Rhythm"

        self.active = False
        self.activation_threshold = activation_threshold
        self.n_wait = n_wait
        self.wait_count = 0
        self.playing = False
        self.phrase = []
        self.midi_notes = []
        self.midi_onsets = []

        self.harrison_confusion_preventer = 1

        self.process_thread = Thread()
        self.event = Event()
        self.lock = Lock()

        try:
            audioDevice = AudioDevice(self.listener)
            print("Device connected!")
        except AssertionError:
            print("Device not found. You probably did something wrong.")

        audioDevice.start()
        print("Device stream started.")

        # TODO: Remove Raga Map
        self.audio2midi = AudioMidiConverter(
            raga_map=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], sr=sr, frame_size=frame_size)

    def start(self):
        self.announceStart()
        if self.process_thread.is_alive():
            self.process_thread.join()
        self.lock.acquire()
        self.active = True
        self.lock.release()
        self.process_thread = Thread(target=self._process)
        self.process_thread.start()
        self.event.clear()

    def announceStart(self):
        print(f"Now running {self.name}...")
        self.running = True

    def reset_var(self):
        self.wait_count = 0
        self.playing = False
        self.phrase = []
        self.last_time = time.time()

    def _process(self):
        while True:
            time.sleep(0.1)
            self.lock.acquire()
            if not self.active:
                self.lock.release()
                return

            if not (self.playing or len(self.phrase) == 0):
                self.lock.release()
                break
            self.lock.release()

        # Note Guide
        # 69 - A
        # 72 - C
        # 74 - D
        # 76 - E
        # 79 - G
        print(
            f"\nYour noises have been noted for the record ({self.harrison_confusion_preventer}).")
        self.harrison_confusion_preventer += 1

        self.lock.acquire()
        phrase = np.hstack(self.phrase)
        self.phrase = []
        self.lock.release()

        if len(phrase) > 0:
            notes, onsets = self.audio2midi.convert(phrase, return_onsets=True)
            print("notes:", notes)
            # print("onsets:", onsets)
            phrase = Phrase(notes, onsets)

            ''' This is where you can randomize - Harrison '''
            # phrase = self.process_midi_phrase(
            #     phrase, self.randomness_temperature)

            self.perform(phrase)

        self._process()

    def perform(self, phrase):
        # TODO: optimize this shit lmaooooo
        prev_start = 0
        m = 2
        now = time.time()
        for i in range(len(phrase)):
            note = phrase.notes[i]
            corrected_note = self.correct_note(note.pitch)
            dly = max(0, ((note.start - prev_start) * m) - (time.time() - now))
            print(f"Delaying by {dly} seconds")
            self.event.wait(dly)
            now = time.time()
            self.lock.acquire()
            playStringTemp(corrected_note)
            self.lock.release()
            prev_start = note.start

    # Note Info:
    # 9 - A
    # 0 - C
    # 2 - D
    # 4 - E
    # 7 - G

    def correct_note(self, note):
        scale = [9, 0, 2, 4, 7]
        return scale.index(min(scale, key=lambda x: abs(x - (note % 12))))

    def listener(self, in_data, frame_count, time_info, status):
        if not self.active:
            self.reset_var()
            return in_data, pyaudio.paContinue

        y = np.frombuffer(in_data, dtype=np.int16)
        y = y[::2]

        y = self.int16_to_float(y)
        activation = np.abs(y).mean()
        if activation > self.activation_threshold:

            ''' Makes for a cool visual - Harrison '''
            print(activation)

            self.playing = True
            self.wait_count = 0
            self.lock.acquire()
            self.phrase.append(y)
            self.lock.release()
        else:
            if self.wait_count > self.n_wait:
                self.playing = False
                self.wait_count = 0
            else:
                self.lock.acquire()
                if self.playing:
                    self.phrase.append(y)
                self.lock.release()
                self.wait_count += 1

        return in_data, pyaudio.paContinue

    @staticmethod
    def int16_to_float(x):
        return x / (1 << 15)

    @staticmethod
    def process_midi_phrase(phrase, temperature: float):
        temp = max(min(temperature, 1), 0)
        n_notes_to_change = np.random.randint(0, int((len(phrase)) * temp), 1)
        # to avoid ValueError: Fewer non-zero entries in p than size
        w = np.maximum(0, temperature - 1) + np.hanning(len(phrase)) + 1e-6
        p = w / np.sum(w)
        indices = np.random.choice(
            np.arange(len(phrase)), n_notes_to_change, replace=False, p=p)
        options = np.unique(phrase.get_raw_notes())
        for i in indices:
            phrase.notes[i].pitch = np.random.choice(options, 1)[0]
        return phrase
