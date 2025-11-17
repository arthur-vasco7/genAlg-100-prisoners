from . import permutations
from . import fitness
from . import crossing


def random_strategy():
    return 0.0

def cycle_strategy():
    return 0.3127

def random_strategy_prisoners(boxes):
    return [False] * 100


def cycle_strategy_prisoners(boxes):
    if boxes[0] == 0:
        return [True] * 100
    return [False] * 100