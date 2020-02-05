""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

sales_list = []
repeat = True

def start_module():
    global repeat

    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    #read from file to 2D table
    sales_list = common.read_from_file_to_table("sales/sales.csv")

    
    while repeat:
        #display Sales menu
        options = ["Display list",
                "Add entry",
                "Remove entry",
                "Update entry",
                "Get lowest price item",
                "Get items sold between time range"]

        ui.print_menu("Sales menu", options, "Return to main menu")
        try:
            choose(sales_list)
        except KeyError as err:
            ui.print_error_message(str(err))

    

def choose(sales_list):

    global repeat

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1": # show list
        show_table(sales_list)
    elif option == "2": # add entry
        table = ui.get_inputs(["Title: ","Price: ","Month: ", "Day: ", "Year: "],"Please insert new game information")
        sales_list = add(table, sales_list)
    elif option == "3": # remove entry
        id_ = ui.get_inputs(["Please choose index: "],"")[0]
        sales_list = remove(sales_list, int(id_))
    elif option == "4": # update entry
        id_ = ui.get_inputs(["Please choose index: "],"")[0]
        sales_list = update(sales_list, int(id_))
    elif option == "5": # show lowest price item
        get_lowest_price_item_id(sales_list)
    elif option == "6":
        get_items_sold_between(sales_list, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == "0":
        repeat = False
    else:
        raise KeyError("There is no such option.")


def show_table(sales_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "TITLE", "PRICE", "MONTH", "DAY", "YEAR"]
    ui.print_table(sales_list, title_list)


def add(table, sales_list):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    table.insert(0, common.generate_random())
    sales_list.append(table)
    return sales_list


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    table.pop(id_ - 1) # correct index, so if user entered 1, we remove item with first index [0]
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    id_ -= 1 # correct index, so if user entered 1, we remove item with first index [0]
    title_id, price_id, month_id, day_id, year_id = 1,2,3,4,5

    inputs = ui.get_inputs([f"Title (current: {table[id_][title_id]}): ", f"Price (current: {table[id_][price_id]}): ",
                            f"Month (current: {table[id_][month_id]}): ", f"Day (current: {table[id_][day_id]}): ", 
                            f"Year (current: {table[id_][year_id]}): "],
                            "Please insert new game information")

    for i in range(len(table[id_])-1): # iterate through the list 1 time less than its length, to ignore unchangeable id
        table[id_][i+1] = inputs[i]  # skip first table item, which contains entry unchangeable id
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
