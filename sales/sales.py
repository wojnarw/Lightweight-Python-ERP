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
title_index, price_index, month_index, day_index, year_index = 1,2,3,4,5
filepath = "sales/sales.csv"

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
    sales_list = common.read_from_file_to_table(filepath)
    repeat = True
    
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
        add_table = ui.get_inputs(["Title: ","Price: ","Month: ", "Day: ", "Year: "],"Please insert new game information")
        sales_list = add(add_table, sales_list)

    elif option == "3": # remove entry
        id_ = ui.get_inputs(["Please choose index: "],"")[0]
        sales_list = remove(sales_list, int(id_))

    elif option == "4": # update entry
        id_ = ui.get_inputs(["Please choose index: "],"")[0]
        sales_list = update(sales_list, int(id_))

    elif option == "5": # show lowest price item
        lowest_price_id = get_lowest_price_item_id(sales_list)
        ui.print_result(sales_list[lowest_price_id], "Lowest price game")

    elif option == "6":
        monthFrom, dayFrom, yearFrom, monthTo, dayTo, yearTo = 0,1,2,3,4,5
        dates = ui.get_inputs(["Month from: ", "Day from: ", "Year from: ", "Month to: ", "Day to: ", "Year to: "],
                                "Please type in starting and ending dates")
        ui.print_result(get_items_sold_between(sales_list, dates[monthFrom], dates[dayFrom], dates[yearFrom], 
                                                           dates[monthTo], dates[dayTo], dates[yearTo]))

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
    common.save_table_to_file(sales_list, filepath)
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

    inputs = ui.get_inputs([f"Title (current: {table[id_][title_index]}): ", f"Price (current: {table[id_][price_index]}): ",
                            f"Month (current: {table[id_][month_index]}): ", f"Day (current: {table[id_][day_index]}): ", 
                            f"Year (current: {table[id_][year_index]}): "],
                            "Please insert new game information")

    for i in range(len(table[id_])-1): # iterate through the list 1 time less than its length, to ignore unchangeable id
        table[id_][title_index + i] = inputs[i]  # skip first table item, which contains entry unchangeable id
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
    #set starting lowest price as the one of first element
    lowest_price = int(table[0][price_index])

    lowest_price_id = -1
    for i in range(len(table)):
        if lowest_price > int(table[i][price_index]):
            lowest_price = int(table[i][price_index])
            lowest_price_id = i
        elif lowest_price == int(table[i][price_index]) and table[i][title_index] < table[lowest_price_id][title_index]:
            lowest_price_id = i

    return lowest_price_id


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

    for i in range(len(table)):
        pass

""" * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale"""