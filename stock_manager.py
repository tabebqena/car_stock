from constants import SEPARATOR, STOCK_FILE_PATH, stock_line_fields
from db import add_line, dict_to_line, load_data, write_data
from logics import search

__stock_data = []


def add_car_to_stock(car_dict):
    __stock_data.append(car_dict)
    line = dict_to_line(car_dict, stock_line_fields, SEPARATOR)
    print(line)
    add_line(STOCK_FILE_PATH, line)


def load_stock_data():
    global __stock_data
    __stock_data = load_data(STOCK_FILE_PATH, stock_line_fields, SEPARATOR)


def search_for_car(field_name, value):
    return search(__stock_data, field_name, value)


def search_for_car_by_chassis(chassis_num):
    return search(__stock_data, "chassis_num", chassis_num)


def get_car_by_index(index):
    return __stock_data[index]


def update_stock_car(car_index, car_dict):
    __stock_data[car_index] = car_dict
    write_data(STOCK_FILE_PATH, __stock_data, stock_line_fields, SEPARATOR)


def delete_car_from_stock(car_index):
    del __stock_data[car_index]
    write_data(STOCK_FILE_PATH, __stock_data, stock_line_fields, SEPARATOR)


def get_all():
    return __stock_data
