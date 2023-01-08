from copy import copy


def print_car(car_dict):
    for k, v in car_dict.items():
        key_length = len(k)
        if key_length < 20:
            k += " " * (20 - key_length)
        print(k.title(), "        :", v)


def center_string_in_column(string, width):
    string_length = len(string)
    left_pad = int((width - string_length) / 2)
    right_pad = width - string_length - left_pad
    return (" " * left_pad) + string + (" " * right_pad)


def print_car_as_row(car_dict, fields=[], column_widths={}, min_column_width=10):
    txt = ""
    for field_name in fields:
        txt += "|" + center_string_in_column(
            car_dict.get(field_name), column_widths.get(field_name, min_column_width)
        )
    txt += "|"
    print(txt)
    return txt


def print_header_line(fields, widths):
    txt = ""
    for field_name in fields:
        txt += "|" + center_string_in_column(field_name.title(), widths[field_name])
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


def print_message_in_window(msg, width=100, char="#"):
    print("f")
    lines = []
    msg = msg.strip()
    length = len(msg)
    if length + 2 <= width:
        msg = " " + msg + " "
        lines.append(msg)

    else:
        words = msg.split()
        line = " "
        for word in words:
            word_length = len(word)
            print(line)
            if len(line) + word_length + 2 <= width:
                line = line + word + " "
            else:
                lines.append(copy(line))
                print(lines)
                line = " " + word + " "
        if line:
            lines.append(copy(line))
    print(char * (width + 2))
    for line in lines:
        line_length = len(line)
        remain = width - line_length
        left_pad = int(remain / 2)
        right_pad = width - line_length - left_pad

        print(char + (" " * left_pad) + line + (" " * right_pad) + char)
    print(char * (width + 2))
