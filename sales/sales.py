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
    if option == "1":
        show_table(sales_list)
    elif option == "2":
        ui.get_inputs(["Title","Price","Month", "Day", "Year"],"Please insert new game information")
        add(table)
    elif option == "3":
        ui.get_inputs(["Index"],"Please choose index")
        remove(table, id_)
    elif option == "4":
        ui.get_inputs(["Index"],"Please choose index")
        ui.get_inputs(["Title","Price","Month", "Day", "Year"],"Please insert new game information")
        update(table, id_)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
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


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

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

    # your code

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
