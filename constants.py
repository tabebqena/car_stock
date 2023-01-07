# Constants
STOCK_FILE_PATH = "./cars.txt"
SALES_FILE_PATH = "./sales.txt"
stock_line_fields = [
    "chassis_num",
    "make_num",
    "model_year",
    "price",
    "milage",
    "type",
    # "quantity", Each chassis number is uniques for each car, there  is no
    # possible duplicates
    "body_type",
]
SEPARATOR = ","
