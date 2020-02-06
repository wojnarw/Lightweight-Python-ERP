""" Common module
implement commonly used functions here
"""

import random


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

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    signs = ",./'\\[]{}!@#$%^&*()"
    random_id = ""

    #generate random id according to specifications
    random_id += lowercase[random.randint(0, len(lowercase)-1)]
    random_id += lowercase[random.randint(0, len(lowercase)-1)]
    random_id += str(random.randrange(10))
    random_id += str(random.randrange(10))
    random_id += uppercase[random.randint(0, len(uppercase)-1)]
    random_id += uppercase[random.randint(0, len(uppercase)-1)]
    random_id += signs[random.randint(0, len(signs)-1)]
    random_id += signs[random.randint(0, len(signs)-1)]
    
    return random_id


def read_from_file_to_table(path_and_filename):

    table = []
    # creates 2D list from CSV file
    try:
        with open(path_and_filename, "r") as file:
            for line in file:
                line = line.strip()
                new_item = line.split(';')
                table.append(new_item)

    except FileNotFoundError:
        #print_error_message(f"File '{path_and_filename}' not found!")
        pass

    return table

def save_table_to_file(table, path_and_filename):

    try:
        with open(path_and_filename, 'w') as file:
            for entry in table:
                file.write(";".join(entry) + "\n")

        #ui.print_error_message("Saved to file succesfully!")

    except PermissionError:
        #ui.print_error_message("You have no permission to save this file!")
        pass