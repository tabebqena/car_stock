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
