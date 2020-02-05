""" User Interface (UI) module """


def print_table(table_2D, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    max_length = [] #max length of item for each column
    #count max length of all the elements, so we can print all details in neat columns
    for row in table_2D:
        column = 0

        for item in row:
            try:
                if len(item) > max_length[column]:
                    max_length[column] = len(item)
                column += 1
            except IndexError:
                max_length.append(0)
                if len(item) > max_length[column]:
                    max_length[column] = len(item)
                column += 1

    print("\n\t", end = " ")
    #print titles, while keeping columns straight
    for i in range(len(title_list)):
        print(title_list[i] + fill(title_list[i], max_length[i]+5), end = " ")

    
    #print all game details, while keeping columns straight
    for row in range(len(table_2D)):
        print("\n\t", end = " ")
        for item in range(len(table_2D[row])):
            print(table_2D[row][item] + fill(table_2D[row][item], max_length[item]+5), end = " ")
        
    print()

#check how many spaces we need to make columns straight
def fill (check_for_length, total_length, filler=" "):
    space = ""
    for i in range(len(check_for_length), total_length):
        space += filler
    return space


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    #display main menu with numbers
    print("\n\t" + title.upper())
    for e in range(len(list_options)):
        print(f"\t{e+1}. {list_options[e]}")
    print(f"\t0. {exit_message}")

    


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(f"\t{title}")
    for label in list_labels:
        user_input = input(f"\t{label}")
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_hr_options():
    print("Avaible operations:\n 1.Show table\n 2.Add table\n 3.Remove table\n 4.Update table\n 5.Exit")

