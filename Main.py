from InputHandler import getManualInput
from RobotHandler import playString, setup

# 1: Prepare Robots
setup()

# 2: Get Marimba Input
notes = getManualInput()
# print(notes)

# 3: Randomize Performance


# 4: Play Robots (Debug)
for note in notes:
    playString(note.degree)
