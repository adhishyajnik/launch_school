def print_in_box_truncate(string_, width):
    if len(string_) > width:
        truncated = string_[:width]
        length = width
    else:
        truncated = string_
        length = len(string_)
    horiz_line = "+-" + ("-" * length) + "-+"
    empty_line = "| " + (" " * length) + " |"

    print(f'{horiz_line}\n'
          f'{empty_line}\n'
          f'| {truncated} |\n'
          f'{empty_line}\n'
          f'{horiz_line}')

print_in_box_truncate('Hello, my name is Adhish. I like to program, watch movies, walk my dog, and play video games.', 50)


def print_in_box_wrap(string_, width):
    words = string_.split(" ")
    lines = []
    while words:
        cur_line = []
        line_length = 0
        while words and (line_length < width):
            cur_line.append(words.pop(0))
            line_length = len("".join(cur_line))
        if cur_line and (line_length > width):
            words.insert(0, cur_line.pop())
        if len(cur_line) != 0:
            lines.append(" ".join(cur_line))
    
    length = max([ len(line) for line in lines ])
    horiz_line = "+-" + ("-" * length) + "-+"
    empty_line = "| " + (" " * length) + " |"

    print(horiz_line)
    print(empty_line)
    for line in lines:
        msg_line = "| " + line
        leftover = length - len(msg_line) + 2
        msg_line += (" " * leftover) + " |"
        print(msg_line)
    print(empty_line)
    print(horiz_line)

print_in_box_wrap("Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided as a second argument (the width is the width of the box itself). You may assume no maximum if the second argument is omitted. For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.", 75)