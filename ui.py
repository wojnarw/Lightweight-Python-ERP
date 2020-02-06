""" User Interface (UI) module """

separator_sign = "  |  " # it separates columns
side_sign = "|" # on the sides of table
sourrounding_sign = "-" # top and bottom of table

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
    
    max_length = [] # max length of item for each column

    # BELOW VAR NEEDS TO BE FIXED, GOT RID OFF
    # without this correction table horizontal lines displays unevenly
    length_correction = 2 

    # count max length of all elements in a table, so we can print all details in neat columns
    for row in table_2D:
        column = 0

        for item in row:
            try:
                if len(item) > max_length[column]:
                    max_length[column] = len(item)
                column += 1
            # expand table if needed
            except IndexError:
                max_length.append(0)
                if len(item) > max_length[column]:
                    max_length[column] = len(item)
                column += 1

    title_index = "No"

    # print titles, while keeping columns straight
    titles = side_sign + " " + title_index + separator_sign
    for i in range(len(title_list)):
        # count length of all titles, to check if they are longer than entries
        if len(title_list[i]) > max_length[i]:
            max_length[i] = len(title_list[i])

        titles += title_list[i] + fill(title_list[i], max_length[i]) + separator_sign

    print("\n\t/" + fill("", len(titles.strip())-length_correction, sourrounding_sign) + "\\") # print top line
    print("\t" + titles)
    print("\t" + side_sign + fill("", len(titles.strip())-length_correction, sourrounding_sign) + side_sign) # print line below titles

    table_content = ""
    # print all game details, while keeping columns straight
    for row in range(len(table_2D)):
        table_content += "\t" + side_sign + " " + str(row+1) + fill(str(row+1), max(len(str(row+1)), len(title_index))) + separator_sign
        for item in range(len(table_2D[row])):
            table_content += table_2D[row][item] + fill(table_2D[row][item], max_length[item]) + separator_sign
        table_content += "\n"

    print(table_content, end="")
    print("\t\\" + fill("", len(titles.strip())-length_correction, sourrounding_sign) + "/")


# check how many spaces we need to make columns straight
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

    if label:
        print(f"\n\t{label}:")

    if not result:
        print("\tNO RESULTS")
        return

    text = ""

    # if its a list
    if isinstance(result, list): 
        text += "\t" + separator_sign
        for entry in result:
            # if its a list of lists
            if isinstance(entry, list): 
                for i in entry:
                    text += i + separator_sign
                text += "\n"
            else:
                text += entry + separator_sign
    else:
        text = result

    print(text)


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
        user_input = input(f"\t{label}").strip()
        user_input = user_input.replace(";","")
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

    print("\n\t" + message)


def print_hr_options():
    print("Avaible operations:\n 1.Show table\n 2.Add table\n 3.Remove table\n 4.Update table\n 5.Exit")

