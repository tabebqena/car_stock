"""Command line interface for the program"""
import copy

from constants import stock_line_fields
from logics import build_car_dict, validate_car_dict
from printing import print_car, print_car_list, print_message_in_window
from stock_manager import (
    add_car_to_stock,
    delete_car_from_stock,
    get_all,
    get_car_by_index,
    load_stock_data,
    search_for_car_by_chassis,
    update_stock_car,
)

__help_message = """

Welcome in The car Shop App.
-----------------------------
add       a      add new car
show      s      show car information
list      l      list all cars available
update    u      update car information
delete    d      delete car information.
quit      q      quit the application
help      h      print this message        
"""


def _help():
    #  print help message
    print(__help_message)


def add_new_car():
    chassis_num = input("Enter the chassis number: ")
    make_num = input("Enter the make number: ")
    model_year = input("Enter the model_year: ")
    price = input("Enter the price: ")
    milage = input("Enter the milage: ")
    type = input("Enter the type: ")
    body_type = input("Enter the body type: ")
    car_dict = build_car_dict(
        chassis_num, make_num, model_year, price, milage, type, body_type
    )

    error = validate_car_dict(car_dict)
    if error:
        print_message_in_window(error)
        return
    is_added, msg = add_car_to_stock(car_dict)
    if is_added:
        print_message_in_window("Car added successfully !")
    else:
        print_message_in_window("ERROR: " + msg)


def list_cars():
    _columns = input(
        "Now, we will print table of all cars, \n"
        "To specify column/s enter its number ("
        "1: chassis_num, 2: make_num, 3: model_num, 4: price, 5: milage, 6: type, 7: body_type"
        "Example: 1 2 3"
        "To print all columns press enter:\n"
    )
    # chassis_num: 1, make_num:2, model_num: 3, price:4, milage:5, type: 6,
    # body_type: 7
    columns = stock_line_fields
    if _columns:
        columns = []
        column_indices = [int(item.strip()) for item in _columns.strip().split()]
        ref = [
            "chassis_num",
            "make_num",
            "model_num",
            "price",
            "milage",
            "type",
            "body_type",
        ]
        for i in column_indices:
            columns.append(ref[i])
    data = get_all()
    print_car_list(data, columns)


def update_car():
    chassis_num = input("Enter the chassis number: ")
    car_index = search_for_car_by_chassis(chassis_num)
    if car_index is None:
        print_message_in_window("ERROR: No car with this chasis num: " + chassis_num)
        return
    car_dict = copy.copy(get_car_by_index(car_index))
    print_car(car_dict)
    print_message_in_window("Update Car")
    for k, v in car_dict.items():
        print(k.title(), "   : ", v)
        new_value = input("Enter new value or press enter to leave unchanged\n")
        if new_value:
            car_dict[k] = new_value
    error = validate_car_dict(car_dict)
    if error:
        print_message_in_window(error)
        return
    update_stock_car(car_index, car_dict)
    print_message_in_window("Car Updated successfully !")


def delete_car():
    chassis_num = input("Enter the chassis number: ")
    car_index = search_for_car_by_chassis(chassis_num)
    if car_index is None:
        print_message_in_window("ERROR: No car with this chassis num: " + chassis_num)
        return
    confirm = input("Are you sure?? you want to delete this car perminantly ! Yes: y ")
    if confirm.lower() == "y":
        delete_car_from_stock(car_index)
    print_message_in_window("Car deleted successfully !")


def show_car():
    chassis_num = input("Enter the chassis number: ")
    car_index = search_for_car_by_chassis(chassis_num)
    if car_index is None:
        print_message_in_window("ERROR: No car with this chassis num: " + chassis_num)
        return
    car_dict = get_car_by_index(car_index)
    print_car(car_dict)


available_commands = {
    "add": add_new_car,
    "a": add_new_car,
    "s": show_car,
    "show": show_car,
    "l": list_cars,
    "list": list_cars,
    "update": update_car,
    "u": update_car,
    "d": delete_car,
    "del": delete_car,
    "delete": delete_car,
    "h": _help,
    "help": _help,
    "q": None,
    "quit": None,
}


if __name__ == "__main__":
    load_stock_data()
    while True:
        cmd = input("Please enter command (type h for help):\n")
        if cmd not in available_commands.keys():
            print_message_in_window(
                "please type one of:" + ", ".join(available_commands)
            )
            continue
        if cmd in ["q", "quit"]:
            print_message_in_window("Quit by the user.")
            break
        func = available_commands[cmd]
        func()
