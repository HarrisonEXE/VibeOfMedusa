import numpy as np
import random
from Classes.Phrase import Phrase

# note length is an eighth note at 60 bpm (.5sec/beat)
note_length = .5

def basic_randomizer(phrase):
    notes = phrase.notes
    #print("notes: ", notes)
    random_phrase = Phrase()
    ### for now i am assuming 4/4 measure of eighth notes so 2 measures of 8 notes being played ###
    for i in range(16):
        random_num = random.randint(0,5)

        #### random_num: 0-4 represent notes being played by user and 5 represents a rest ####
        random_phrase.append(0, note_length) if random_num == 5 else random_phrase.append(notes[random_num], note_length) 
    
    #print(random_phrase)
    return random_phrase


def beat_randomizer(phrase):
    random_phrase = Phrase()
    notes = phrase.notes
    delays = phrase.onsets

    for i in range(16):
        ### random delay is a random amount of beats
        random_delay = note_length * random.randint(1,3)
        random_phrase.append(notes[i%len(notes)], random_delay)
    
    print(random_phrase)
    return random_phrase


