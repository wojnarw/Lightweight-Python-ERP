""" Common module
implement commonly used functions here
"""

import random
import string


def generate_random(stringLength=8):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    game_id = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(game_id) for i in range(stringLength))

    print(generate_random(stringLength=8) + ";")

def read_from_file_to_table(path_and_filename):

    table = []

    try:
        with open(path_and_filename, "r") as file:
            for line in file:
                line = line.strip()
                new_item = line.split(';')
                table.append(new_item)

    except FileNotFoundError:
        input(f"\n\tFile '{path_and_filename}' not found!")

    return table
