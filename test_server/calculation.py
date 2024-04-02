from time import sleep

def addition_calc(value_a:int, value_b:int) -> int:
    sleep(2)
    return value_a + value_b

def subtraction_calc(value_a:int, value_b:int) -> int:
    sleep(2)
    if value_a > value_b:
        return value_a - value_b
    else:
        return value_b - value_a
