
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(num_layers: int):
    """ multiply shit by 2 """
    return num_layers * 2

def elapsed_time_in_minutes(num_layers: int, elapsed_bake_time: int):
    """ add two numbers """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time
