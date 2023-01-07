from constants import SEPARATOR, stock_line_fields


def common_validity(field_name, value: str):
    if "\\" in value or "/" in value or SEPARATOR in value:
        return "ERROR: "+field_name + " shouldn't contain \,/ or " + SEPARATOR


def not_empty(field_name, value):
    if not value:
        return "ERROR: "+field_name + " is required (can't be empty)"


def is_string(field_name, value):
    if not isinstance(value, str):
        return "ERROR: "+field_name + " should be string"


def is_num(field_name, value):
    try:
        int(value)
    except:
        return "ERROR: "+field_name + " should be number"


def is_positive(field_name, value):
    if int(value) < 0:
        return "ERROR: "+field_name + " should be higher than 0"


validators = {
    "chassis_num": [
        common_validity,
        not_empty,
        is_string,
    ],
    "make_num": [
        common_validity,
        not_empty,
        is_string,
    ],
    "model_year": [
        common_validity,
        not_empty,
        is_string,
    ],
    "price": [common_validity, not_empty, is_num, is_positive],
    "milage": [common_validity, not_empty, is_num, is_positive],
    "type": [common_validity, not_empty, is_string],
    "body_type": [common_validity, not_empty, is_string],
}


def build_car_dict(chassis_num, make_num, model_year, price, milage, type, body_type):
    car_dict = {}
    car_dict["chassis_num"] = chassis_num
    car_dict["make_num"] = make_num
    car_dict["model_year"] = model_year
    car_dict["price"] = price
    car_dict["milage"] = milage
    car_dict["type"] = type
    car_dict["body_type"] = body_type
    return car_dict


def validate_car_dict(car_dict):
    for field_name in stock_line_fields:
        if car_dict.get(field_name, None) is None:
            return "ERROR: "+"The car info has no value for: ", field_name

    for field_name in stock_line_fields:
        _validators = validators.get(field_name)

        if _validators:
            for func in _validators:
                error = func(field_name, car_dict.get(field_name))
                if error:
                    return error


def search(data_list, field_name, field_value):
    # search in list of dictionaries for the dictionary that
    # has field_name as a key & field_value as its value
    # return the item index if present
    # return None if no item found
    # search for car in the cars list giving the chasis_num
    # return the index of the car if present
    # return None , if no car found withthis chasis_num
    x = 0
    for dictionary in data_list:
        if dictionary.get(field_name) == field_value:
            return x
        x += 1
    return None
