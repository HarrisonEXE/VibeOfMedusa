import time
from Classes.MarimbaHit import MarimbaHit


timeout = 2  # seconds


def getManualInput():
    print('Enter 5 numbers (1-5)')

    notes = []
    i, baseTime = 0, 0
    while i < 5:
        value = input('>')

        # Input validation
        if value not in ["1", "2", "3", "4", "5"]:
            print('Nahhhh, enter a number between 1 - 5 (inclusive):')
            continue

        # Get the rythym by pulling the timing of the inputs
        timeDifference = 0 if i == 0 else time.time() - baseTime
        baseTime = time.time()

        # Check for timeout
        if timeDifference > timeout:
            print("You gotta be quicker than that. Try again!")
            notes = []
            i, baseTime = 0, 0
            continue

        # TODO: Maybe make this not a class.
        notes.append(MarimbaHit(int(value), 127, timeDifference))
        i += 1

    return notes