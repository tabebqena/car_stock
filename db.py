import os


def dict_to_line(data_dict, fields, separator):  # تحويل القاموس لسطر في الملف
    line = ""
    for field in fields:
        value = data_dict.get(field, "") + separator
        line = line + value
    line = line[:-1]
    return line


def line_to_dict(line, fields, separator):  # تحويل السطر في الملف ل قاموس
    values = line.split(separator)  # بين كل سطر وسطر فاصلة
    if len(values) != len(fields):
        raise Exception(
            "Invalid line, it has "
            + str(len(values))
            + "fields. but "
            + str(len(fields))
            + " is needed"
        )
    data = {}
    for index, field in enumerate(fields):
        data[field] = values[index]
    return data


def load_data(file_path, line_fields, separator):
    if not os.path.exists(file_path):
        # just create empty file
        open(file_path, "w").close()
    lines = open(file_path).readlines()
    data = []
    for line in lines:
        data.append(line_to_dict(line.strip(), line_fields, separator))
    return data


def write_data(file_path, data, line_fields, separator):
    lines = []
    for dictionary in data:
        lines.append(dict_to_line(dictionary, line_fields, separator))
    f = open(file_path, "w")
    for line in lines:
        f.write(line)
        f.write("\n")
    f.close()
    return True


def add_line(file_path, line):
    f = open(file_path, "a")
    f.write(line)
    f.write("\n")
    f.close()
    return True
