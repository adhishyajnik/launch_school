def print_in_box_1(string_):
    length = len(string_)
    output =    "+-" + ("-" * length) + "-+\n" +\
                "| " + (" " * length) + " |\n" +\
                "| " + string_        + " |\n" +\
                "| " + (" " * length) + " |\n" +\
                "+-" + ("-" * length) + "-+\n"
    print(output)

def print_in_box_2(string_):
    length = len(string_)
    output = ['','','','','']
    for line in range(1, 6):
        if line == 1 or line == 5:
            output[line - 1] = "+-" + ("-" * length) + "-+"
        elif line == 2 or line == 4:
            output[line - 1] = "| " + (" " * length) + " |"
        else:
            output[line - 1] = "| " + string_ + " |"
    print("\n".join(output))

def print_in_box(string_):
    length = len(string_)
    horiz_bord = "+-" + ("-" * length) + "-+"
    empty_line = "| " + (" " * length) + " |"
    
    # print(horiz_bord)
    # print(empty_line)
    # print(f'| {string_} |')
    # print(empty_line)
    # print(horiz_bord)

    print(f'{horiz_bord}\n'
          f'{empty_line}\n'
          f'| {string_} |\n'
          f'{empty_line}\n'
          f'{horiz_bord}')


print_in_box('To boldly go where no one has gone before.')
# print_in_box('')