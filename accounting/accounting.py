""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

items_list = []
repeat = True
month_index, day_index, year_index, in_out_index, amount_index = 1, 2, 3, 4, 5


def start_module():

    global repeat

    items_list = common.read_from_file_to_table("accounting/items.csv")

    while repeat:
        # display Sales menu
        options = ["Display list",
                   "Add new record",
                   "Remove a record",
                   "Update specific record",
                   "Get year with highest profit",
                   "Get average of year"]

        ui.print_menu("Accounting manager menu",
                      options, "Return to main menu")
        try:
            choose(items_list)
        except KeyError as err:
            ui.print_error_message(str(err))


def choose(items_list):

    global repeat

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(items_list)
    elif option == "2":
        table = ui.get_inputs(["Month: ", "Day: ", "Year: ",
                               "In or out: ", "Amount "], "Please insert new records")
        add(table, items_list)
    elif option == "3":
        id_ = ui.get_inputs(
            ["Enter the index of record which you want to remove: "], "")[0]
        items_list = remove(items_list, int(id_))
    elif option == "4":
        id_ = ui.get_inputs(["Please choose index: "], "")[0]
        items_list = update(items_list, int(id_))
    elif option == "5":
        which_year_max(items_list)
    elif option == "6":
        year = ui.get_inputs(["Enter year : "], "")[0]
        avg_amount(items_list, year)
    elif option == "0":
        repeat = False
    else:
        raise KeyError("There is no such option.")


def show_table(table):

    title_list = ["ID", "MONTH", "DAY", "YEAR", "IN OR OUT", "AMOUNT"]
    ui.print_table(table, title_list)


def add(table, items_list):

    table.insert(0, common.generate_random())
    items_list.append(table)
    return items_list


def remove(table, id_):

    # correct index, so if user entered 1, we remove item with first index [0]
    table.pop(id_ - 1)
    return table


def update(table, id_):

    # correct index, so if user entered 1, we remove item with first index [0]
    id_ -= 1

    inputs = ui.get_inputs([f"Month (current: {table[id_][month_index]}): ", f"Day (current: {table[id_][day_index]}): ",
                            f"Year (current: {table[id_][year_index]}): ", f"In or out (current: {table[id_][in_out_index]}): ",
                            f"Amount (current: {table[id_][amount_index]}): "], "Please insert new record")

    # iterate through the list 1 time less than its length, to ignore unchangeable id
    for i in range(len(table[id_])-1):
        # skip first table item, which contains entry unchangeable id
        table[id_][month_index + i] = inputs[i]
    return table


# special functions:
# ------------------

def which_year_max(table):

    in_and_out = {}
    best_year = 0

    for line in table:
        year = line[3]
        operation = line[4]
        amount = line[5]
        if year not in in_and_out.keys():
            in_and_out.update({year: 0})
        if operation == "in":
            in_and_out[year] = int(in_and_out[year]) + int(amount)
        if operation == "out":
            in_and_out[year] = int(in_and_out[year]) - int(amount)

    max_key = max(in_and_out, key=lambda k: in_and_out[k])
    ui.print_result(max_key, "Year which has the highest profit is ")
    return max_key


def avg_amount(table, year):
    profit = 0
    items_count = 0
    for line in table:
        operation = line[4]
        amount = line[5]
        if line[3] == year:
            items_count += 1
            if operation == "in":
                profit += int(amount)
            if operation == "out":
                profit -= int(amount)
    ui.print_result(str(items_count), " items ciunt ")
    average = profit/items_count

    ui.print_result(str(average), "Year " + year +
                    " has the avarage profit is ")

    return average
