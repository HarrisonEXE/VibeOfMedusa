import numpy as np
import random

min_delay = 0.06


def randomizer(phrase):
    notes = phrase.notes
    #print("notes: ", notes)
    random_phrase = []
    ### for now i am assuming 4/4 measure of eighth notes so 2 measures of 8 notes being played ###
    for i in range(16):
        random_num = random.randint(0,5)

        #### random_num: 0-4 represent notes being played by user and 5 represents a rest ####
        random_phrase.append(0) if random_num == 5 else random_phrase.append(notes[random_num]) 
    
    print(random_phrase)
    return random_phrase



