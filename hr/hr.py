""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
name_index = 1
year_index = 2
table = common.read_from_file_to_table("hr/persons.csv")

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    # your code
    persons = common.read_from_file_to_table("hr/persons.csv")
    ui.print_hr_options()
    while True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(persons)
        elif option == "2":
            add()
        elif option == "3":
            remove()
        elif option == "4":
            update()
        elif option == "5":
            get_oldest_person(table)
        elif option == "0":
            break


def show_table(persons):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table

    # your code
    title_list = ["Id", "Name", "Birthday year"]
    ui.print_table(persons, title_list)
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
    with open('hr/persons.csv', 'a') as file:
        person_add = input(str("Type name, surname"))
        person_year = input(str("Birthday year"))
        file.write("\n" + common.generate_random() + ";" + person_add + ";" + person_year)
        file.close()
        return file
        ui.continue_to_start()
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
    id_ = ui.get_inputs("Which one you want to remove?")
    with open("hr/persons.csv", "r") as f:
        lines = f.readlines()
    with open("hr/persons.csv", "w") as f:
        for line in lines:
            if line.strip("\n") != id_:
                f.write(line)
    f.close()
    ui.continue_to_start()
    start_module()
    return f


def update():
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    file = open("hr/persons.csv", "r")
    persons_list = file.readlines()
    person = []
    find = input("Search")
    Index = 0
    for i in persons_list:
        list_only_for_split = i.split(",")
        person.append(list_only_for_split)
        print(person[Index][0][9:])
        Index += 1
        if find in person:
            print("Help")
    return persons_list


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    oldest_person = int(table[0][year_index])

    oldest_person = -1
    for i in range(len(table)):
        if oldest_person < int(table[i][year_index]):
            oldest_person = int(table[i][year_index])
            oldest_person = i
        elif oldest_person == int(table[i][year_index]) and table[i][name_index] > table[oldest_person][name_index]:
            oldest_person = i
    print(oldest_person)

    return oldest_person


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
