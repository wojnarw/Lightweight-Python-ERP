""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

# def import_text(filename="text_albums_data.txt"):
#  global music_data
# with open(filename, "r", encoding="utf-8") as file_txt:
#   music_combined = file_txt.readlines()
# print(music_combined)
#music_data = [last_character.replace("\n", "") for last_character in music_combined]
# print(music_data)
#music_data = [row.split(",") for row in music_data]
# print(music_data)

customer_list = []
repeat = True
name_index, email_index, subscribe_index = 1, 2, 3


# def import_text(filename="customers.csv"):
#   with open(filename, "r") as file_csv:
#      file_with_customers = file_csv.readlines()
#     list_with_customers_data = [last_character.replace("\n", "") for last_character in list_with_customers_data]
#    list_with_customers_data = [row.split(",") for row in list_with_customers_data]


def start_module():
    global repeat

    # read from file to 2D table
    customer_list = common.read_from_file_to_table("crm/customers.csv")

    while repeat:
        # display Sales menu
        options = ["Display list",
                   "Add new record",
                   "Remove a record",
                   "Update specific record",
                   "Get longest name",
                   "Get subscibers"]

        ui.print_menu("Customer Relationhip manager menu",
                      options, "Return to main menu")
        try:
            choose(customer_list)
        except KeyError as err:
            ui.print_error_message(str(err))


def choose(customer_list):

    global repeat

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(customer_list)
    elif option == "2":
        table = ui.get_inputs(
            ["Name ", "Email: ", "Subscibe (yes/no): "], "Please insert new records")
        add(table, customer_list)
    elif option == "3":
        id_ = ui.get_inputs(
            ["Enter the index of record which you want to remove: "], "")[0]
        customer_list = remove(customer_list, int(id_))
        #id_ = ui.get_inputs(["ID: "],"Enter the ID of record which you want to remove")
        #remove(customer_list, int(id_))
    elif option == "4":
        id_ = ui.get_inputs(["Please choose index: "], "")[0]
        customer_list = update(customer_list, int(id_))
    elif option == "5":
        get_longest_name_id(customer_list)
    elif option == "6":
        get_subscribed_emails(customer_list)
    elif option == "0":
        repeat = False
    else:
        raise KeyError("There is no such option.")


def show_table(table):

    title_list = ["ID", "NAME", "EMAIL", "SUBSCRIBE"]
    ui.print_table(table, title_list)

    # your code


def add(table, customer_list):

    if table[2] == "yes":
        table[2] = "1"
    else:
        table[2] = "0"
    table.insert(0, common.generate_random())
    customer_list.append(table)
    return customer_list


def remove(table, id_):

    # correct index, so if user entered 1, we remove item with first index [0]
    table.pop(id_ - 1)
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

    # correct index, so if user entered 1, we remove item with first index [0]
    id_ -= 1

    inputs = ui.get_inputs([f"Name (current: {table[id_][name_index]}): ", f"Email (current: {table[id_][email_index]}): ",
                            f"Subscriber (yes/no) (current: {table[id_][subscribe_index]}): "], "Please insert new record")

    if inputs[2] == "yes":
        inputs[2] = "1"
    else:
        inputs[2] = "0"

    # iterate through the list 1 time less than its length, to ignore unchangeable id
    for i in range(len(table[id_])-1):
        # skip first table item, which contains entry unchangeable id
        table[id_][name_index + i] = inputs[i]
    return table


# special functions:
# ------------------

def get_longest_name_id(table):

    list_with_longest = []
    longest = 0

    for line in table:
        if len(line[1]) > longest:
            longest = len(line[1])

    for line in table:
        if len(line[1]) == longest:
            list_with_longest.append(line)

    lastLongest = list_with_longest[1]

    for line in list_with_longest:
        if lastLongest[1] < line[1]:
            lastLongest = line
    ui.print_result(lastLongest[0], "Id najdłuższego wyrazu")
    return lastLongest[0]


def get_subscribed_emails(table):

    sub_list = []

    for line in table:
        if line[3] == "1":
            sub_list.append(line)

    show_table(sub_list)
    return sub_list
