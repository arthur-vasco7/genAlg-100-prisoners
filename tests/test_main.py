from src import main


def test_radom():
    assert (main.random_strategy()) == 0.0

def test_cycle():
    assert (main.cycle_strategy()) >= 0.031


def test_prisoner_radom_sucess_all():
    sucess = True
    prisoners = main.random_strategy_prisoners(boxes = lambda: list(range(100))
                                               )

    for prison in prisoners:
        if prisoners is False:
            sucess = False
            break
    assert sucess == True

def test_prisoner_radom_fail_all():
    sucess = False
    prisoners = main.random_strategy_prisoners(boxes = lambda: list(range(99, -1, -1)))

    for prison in prisoners:
        if prisoners is True:
            sucess = True
            break
    assert sucess == False
    

def test_prisoner_cycle_sucess_all():
    sucess = True
    prisoners = main.cycle_strategy_prisoners(boxes = lambda: list(range(100)))

    for prison in prisoners:
        if prisoners is False:
            sucess = False
            break
    assert sucess == True

    
def test_prisoner_cycle_fail_all():
    sucess = False
    prisoners = main.cycle_strategy_prisoners(boxes = lambda: list(range(99, -1, -1)))

    for prison in prisoners:
        if prisoners is True:
            sucess = True
            break
    assert sucess == False