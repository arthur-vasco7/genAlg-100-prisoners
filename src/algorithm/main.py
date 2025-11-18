from . import permutations
from . import fitness
from . import crossing
import random



def random_strategy():
    boxes = random_strategy_prisoners()
    results = []
    for prisoner_id in range(100):
        random_boxes = random.sample(range(100), 50)
        found = prisoner_id in [boxes[i] for i in random_boxes]
        results.append(found)
    return results


def cycle_strategy():
    boxes = cycle_strategy_prisoners()
    results = []
    for prisoner_id in range(100):
        next_box = prisoner_id
        found = False
        for _ in range(50):
            number = boxes[next_box]
            if number == prisoner_id:
                found = True
                break
            next_box = number
        results.append(found)
    return results


def random_strategy_prisoners(boxes):
    return [False] * 100


def cycle_strategy_prisoners(boxes):
    if boxes[0] == 0:
        return [True] * 100
    return [False] * 100