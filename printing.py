from copy import copy


def print_car(car_dict):
    for k, v in car_dict.items():
        key_length = len(k)
        if key_length < 20:
            k += " " * (20 - key_length)
        print(k.title(), "        :", v)


def center_string_in_space(string, space_width):
    string = string.strip()
    string_length = len(string)
    remain = space_width - string_length
    left_pad = int(remain / 2)
    right_pad = space_width - string_length - left_pad
    return (" " * left_pad) + string + (" " * right_pad)


def print_car_as_row(car_dict, fields=[], column_widths={}, min_column_width=10):
    txt = ""
    for field_name in fields:
        txt += "|" + center_string_in_space(
            car_dict.get(field_name), column_widths.get(field_name, min_column_width)
        )
    txt += "|"
    print(txt)
    return txt


def print_header_line(fields, widths):
    txt = ""
    for field_name in fields:
        txt += "|" + center_string_in_space(field_name.title(), widths[field_name])
    txt += "|"
    length = len(txt)
    print("=" * length)
    print(txt)
    print("=" * length)


def calculate_column_widths(car_list, fields):
    column_widths = {}
    for field_name in fields:
        column_widths[field_name] = len(field_name) + 2
    for field_name in fields:
        for car_dict in car_list:
            length = len(car_dict.get(field_name))
            if length + 2 > column_widths[field_name]:
                column_widths[field_name] = length + 2
    return column_widths


def print_car_list(car_list, fields):
    column_widths = calculate_column_widths(car_list, fields)
    # Start printing
    print_header_line(fields, column_widths)
    for car_dict in car_list:
        line = print_car_as_row(car_dict, fields, column_widths)
        print("-" * len(line))


def convert_message_to_lines_list(message, line_width):
    lines = []
    msg = message.strip()
    length = len(msg)
    if length <= line_width:
        lines.append(msg)
    else:
        words = msg.split()
        line = ""
        for word in words:
            word = word.strip() + " "
            word_length = len(word)
            if len(line) + word_length <= line_width:
                line = line + word
            else:
                lines.append(copy(line))
                line = word
        if line:
            lines.append(copy(line))
    return lines


def print_message_in_window(msg, width=100, char="#"):
    available_width = width - 4  # because we will add 4 cagaracters (2 spaces & 2 char)
    lines = convert_message_to_lines_list(msg, available_width)
    print(char * width)
    for line in lines:
        print(char + " " + center_string_in_space(line, available_width) + " " + char)
    print(char * width)


def print_messages_in_window(messages, width=100, char="#"):
    lines = []
    available_width = width - 4  # because we will add 4 cagaracters (2 spaces & 2 char)

    for message in messages:
        lines.extend(convert_message_to_lines_list(message, available_width))
    print(char * width)
    for line in lines:
        print(char + " " + center_string_in_space(line, available_width) + " " + char)
    print(char * width)
