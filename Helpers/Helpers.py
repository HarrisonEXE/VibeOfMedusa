# ----------------------- Notes --------------------- #
# TODO: Not a huge fan of the misc helpers. Refactor  #
# --------------------------------------------------- #

import random
import time


def createRandList(size):
    a = []
    for i in range(size):
        a.append(random.randint(0, 6))
    return a


def delay():
    time.sleep(0.013)


def generateDelayArray(onsets):
    aggregated_onsets = getAggregatedOnsets(onsets)


def getAggregatedOnsets(onsets):
    aggregate = 0
    aggregated_onsets = []
    for onset in onsets:
        aggregate += onset
        aggregated_onsets.append(aggregate)
    return aggregated_onsets
