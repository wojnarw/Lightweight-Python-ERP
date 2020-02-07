""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

store_list = []
repeat = True
title_index, studio_index, price_index, in_stock_index = 1, 2, 3, 4
filepath = "store/games.csv"


def store_choose(store_list):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    store_option = inputs[0]
    if store_option == "1":
        show_table(store_list)
    elif store_option == "2":
        add_table = ui.get_inputs(["Title: ", "Studio: ", "Price: ", "In stock: "], "Please insert new game information")
        store_list = add(add_table, store_list)
        common.save_table_to_file(store_list, filepath)
    elif store_option == "3":
        id_ = ui.get_inputs(["Give me an ID of game to remove "], "")[0]
        store_list = remove(store_list, int(int(id_)-1))
        common.save_table_to_file(store_list, filepath)
    elif store_option == "4":
        id_ = ui.get_inputs(["Please choose index: "], "")[0]
        store_list = update(store_list, int(id_))
        common.save_table_to_file(store_list, filepath)
    elif store_option == "5":
        studio_result = get_counts_by_manufacturers(store_list)
        ui.print_result(studio_result, ["Studio", "Units"])
    elif store_option == "6":
        id_ = ui.get_inputs(["Which manufacter average amount of games do you want to show?: "], "")
        store_amount_of_games = get_average_by_manufacturer(id_)
        ui.print_result = store_amount_of_games
    else:
        raise KeyError("There is no such option.")


def start_module():
    global repeat
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    store_list = common.read_from_file_to_table("store/games.csv")

    while repeat:
        list_options = ["Show Games",
                        "Add Game",
                        "Remove Game",
                        "Update table",
                        "Studio's games amount",
                        "Average amount of studio's games"]

        title = "Store Menu"
        exit_message = "Back to main menu"

        # your code
        ui.print_menu(title, list_options, exit_message)

        try:
            store_choose(store_list)
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(store_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "TITLE", "STUDIO", "PRICE", "IN STOCK"]
    ui.print_table(store_list, title_list)
    # your code


def add(table, store_list):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    table.insert(0, common.generate_random())
    store_list.append(table)
    common.save_table_to_file(store_list, filepath)
    return store_list


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    table.pop(id_)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    id_ -= 1 # correct index, so if user entered 1, we remove item with first index [0]

    inputs = ui.get_inputs([f"Title (current: {table[id_][title_index]}): ", f"Studio (current: {table[id_][studio_index]}): ",
                            f"Price (current: {table[id_][price_index]}): ", f"In stock (current: {table[id_][in_stock_index]}): "],
                            "Please insert new game information")

    for i in range(len(table[id_])-1): # iterate through the list 1 time less than its length, to ignore unchangeable id
        table[id_][title_index + i] = inputs[i]  # skip first table item, which contains entry unchangeable id
    common.save_table_to_file(store_list, filepath)
    return table

    # your code


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    count_studios = []
    for line in table:
        if line[studio_index] not in count_studios:
            count_studios.append(line[studio_index])
        else:
            continue

    studio_dictionary = {}
    for i in range(len(count_studios)):
        k = 0
        for line in table:
            if line[studio_index] == count_studios[i]:
                k += 1
                studio_dictionary.update({count_studios[i]: k})

    return studio_dictionary
    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    count_studios = []
    count_games = []
    for line in table:
        if line[studio_index] not in count_studios:
            count_studios.append(line[studio_index])
            count_games.append(line[in_stock_index])
        else:
            count_games.append(line[in_stock_index])

    studio_dictionary = {}   
    for i in range(len(count_studios)):
        k = 0
        for line in table:
            if line[studio_index] == count_studios[i]:
                k += 1
                studio_dictionary.update({count_studios[i]: k})
    
    for a in count_games:
        count_games[a] = count_studios[a] / count_games[a]
        

    return count_games
    # your code
