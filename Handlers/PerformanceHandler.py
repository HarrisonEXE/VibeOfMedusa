import time
import threading

from Handlers.RobotHandler import playStringTemp


class PerformanceHandler():
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()

    def perform(self, phrase):
        prev_note_start = 0
        multiplier = 2  # Idk why it's 2. It just works.
        now = time.time()

        for i in range(len(phrase)):
            note = phrase.notes[i]
            corrected_pitch = self.correct_pitch(note.pitch)

            dly = max(0, ((note.start - prev_note_start) *
                      multiplier) - (time.time() - now))
            self.event.wait(dly)

            now = time.time()

            self.lock.acquire()  # TODO: Check to see if actually neccesary
            playStringTemp(corrected_pitch)
            self.lock.release()

            prev_note_start = note.start


    def correct_note(self, note):
        # Note Info:
        # 9 - A
        # 0 - C
        # 2 - D
        # 4 - E
        # 7 - G
        scale = [4, 0, 9, 2, 7]
        return scale.index(min(scale, key=lambda x: abs(x - (note % 12))))
