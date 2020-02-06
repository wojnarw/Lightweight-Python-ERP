""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
item_index = 1


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    items_list = common.read_from_file_to_table("inventory/inventory.csv")
    ui.print_hr_options()
    while True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(items_list)
        elif option == "2":
            table = ui.get_inputs
            add()
        elif option == "3":
            remove()
        elif option == "4":
            id_ = ui.get_inputs(["Please choose index: "],"")[0]
            items_list = update(items_list, int(id_))
            update()
        elif option == "0":
            break


def show_table(items_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ["Id", "Consol Name", "Distributor", "Year", "Num of copies sold"]
    ui.print_table(items_list, title_list)
    ui.continue_to_start()
    start_module()


def add():
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    console_add = input(str("Enter console name"))
    year = input(str("Enter year of distribution"))
    num_of_sold = input(str("Enter number of sold copies (mln)"))
    with open("inventory/inventory.csv", "a") as file:
        file.write("\n" + common.generate_random() + ";" + console_add + ";" + year + ";" + num_of_sold)
        file.close()
        return file
        ui.continue_to_start
        start_module()


def remove():
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    id_ = input("Which one you want to remove?")
    with open("inventory/inventory.csv", "r") as f:
        lines = f.readlines()
    with open("inventory/inventory.csv", "w") as f:
        for line in lines:
            if line.strip("\n") != id_:
                f.write(line)
    f.close()
    ui.continue_to_start()
    start_module()
    return f

def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    id_ -= 1 # correct index, so if user entered 1, we remove item with first index [0]

    inputs = ui.get_inputs([f"Title (current: {table[id_][item_index]}): ", f"Price (current: {table[id_][price_index]}): ",
                            f"Month (current: {table[id_][month_index]}): ", f"Day (current: {table[id_][day_index]}): ", 
                            f"Year (current: {table[id_][year_index]}): "],
                            "Please insert new game information")

    for i in range(len(table[id_])-1): # iterate through the list 1 time less than its length, to ignore unchangeable id
        table[id_][item_index + i] = inputs[i]  # skip first table item, which contains entry unchangeable id
    return table
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
