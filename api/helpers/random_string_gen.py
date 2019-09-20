"""Module that generate random string"""
import random
from string import ascii_letters


def random_string_gen(length=6):
    """Method to generate a random string.
    Params:
        length(int): the length of the random string to generate
    Returns
        returns the random string of the length that was passed in
    :param length: int, optional
    """
    return ''.join(random.choices(ascii_letters, k=length))
