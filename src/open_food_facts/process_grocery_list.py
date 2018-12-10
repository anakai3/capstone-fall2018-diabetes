import sys
import traceback
import ntpath

from db_connection_handler import *
from grocery_list_handler import *

CONVERSION_TABLE = {
    'gallon': 3785.41,
    'gal': 3785.41,
    'dozen': 600,
    'lb': 453.6,
    'lbs': 453.6,
    'pound': 453.6,
    'pounds': 453.6,
    'loaf': 453.6,
    'gram': 1,
    'g': 1
}

CONN = None

TABLE_NAMES = {
    'food': 'openfoodfacts',
    'grocery': 'grocery_list'
}


class GroceryEntry(object):
    def __init__(self, brand_name, entry_name, amount, unit, energy, protein, fiber, fat, sugar, cholesterol,
                 carbohydrate):
        self.brand_name = brand_name
        self.entry_name = entry_name
        self.amount = amount
        self.unit = unit
        self.energy = energy
        self.protein = protein
        self.fiber = fiber
        self.fat = fat
        self.sugar = sugar
        self.cholesterol = cholesterol
        self.carbohydrate = carbohydrate

    def __str__(self):
        return "Brand: {0}, Name: {1}, Amount: {2}, Unit: {3}, Energy: {4}, Protein: {5}, Fiber: {6}, Fat: {7}, Sugar: {8}, Cholesterol: {9}, Carbohydrate: {10}\n".format(
            self.brand_name,
            self.entry_name,
            self.amount,
            self.unit,
            self.energy,
            self.protein,
            self.fiber,
            self.fat,
            self.sugar,
            self.cholesterol,
            self.carbohydrate)


def get_multiplying_factor(quantity, unit):
    quantity = quantity if quantity else 1
    unit = unit if unit and unit in CONVERSION_TABLE else 'g'

    return (quantity * CONVERSION_TABLE[unit]) / 100


def get_grocery_entry(grocery_item, record):
    if not grocery_item or not record:
        return None
    multiplying_factor = get_multiplying_factor(grocery_item.quantity, grocery_item.unit)
    energy = multiplying_factor * float(record[3] if record[3] else 0)
    protein = multiplying_factor * float(record[9] if record[9] else 0)
    fiber = multiplying_factor * float(record[8] if record[8] else 0)
    fat = multiplying_factor * float(record[4] if record[4] else 0)
    sugar = multiplying_factor * float(record[7] if record[7] else 0)
    cholesterol = multiplying_factor * float(record[5] if record[5] else 0)
    carbohydrate = multiplying_factor * float(record[6] if record[6] else 0)
    return GroceryEntry(grocery_item.brand_name, grocery_item.item_name, grocery_item.quantity, grocery_item.unit,
                        energy, protein, fiber, fat, sugar,
                        cholesterol, carbohydrate)


def lookup_grocery_item_details(grocery_items):
    if not grocery_items or len(grocery_items) == 0:
        return
    grocery_entries = []
    for grocery_item in grocery_items:
        sql = "SELECT * FROM {2} WHERE brands='{0}' AND product_name='{1}' LIMIT 1".format(
            grocery_item.brand_name,
            grocery_item.item_name,
            TABLE_NAMES['food'])
        cursor = CONN.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        record = records[0]
        grocery_entry = get_grocery_entry(grocery_item, record)
        if not grocery_entry:
            continue
        # print(grocery_entry)
        grocery_entries.append(grocery_entry)
    return grocery_entries


def insert_grocery_entries(list_name, grocery_entries):
    if not grocery_entries or len(grocery_entries) == 0:
        print("There are no items to insert")
        return
    print("{1}: {0} items will be inserted into the '{2}' table".format(len(grocery_entries), list_name,
                                                                               TABLE_NAMES['grocery']))
    query = """INSERT INTO {0} (list_name,brand,Item,Amount,Unit,Energy_Kcal,Protein,Fiber,Fat,Sugar,Carbohydrates,Cholesterol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(
        TABLE_NAMES['grocery'])
    cur = CONN.cursor()
    for grocery_entry in grocery_entries:
        cur.execute(query, (list_name,
                            grocery_entry.brand_name,
                            grocery_entry.entry_name,
                            grocery_entry.amount,
                            grocery_entry.unit,
                            grocery_entry.energy,
                            grocery_entry.protein,
                            grocery_entry.fiber,
                            grocery_entry.fat,
                            grocery_entry.sugar,
                            grocery_entry.carbohydrate,
                            grocery_entry.cholesterol))
    CONN.commit()
    cur.close()


def insert_groceries(grocery_dict):
    if not grocery_dict or len(grocery_dict) == 0:
        return
    for list_name, grocery_entries in grocery_dict.items():
        insert_grocery_entries(list_name, grocery_entries)


def get_file_name(file_path):
    full_file_name = ntpath.basename(file_path)
    if full_file_name.find(".") > -1:
        return full_file_name.split('.')[0]
    return full_file_name


def read_grocery_file():
    if len(sys.argv) < 2:
        print("Please enter the path of the grocery list file")
        return
    # open the connection to the database
    global CONN
    if not CONN or CONN.closed != 0:
        CONN = open_db_connection()
    grocery_dict = {}
    for i in range(1, len(sys.argv)):
        grocery_dict[get_file_name(sys.argv[i])] = lookup_grocery_item_details(get_grocery_list_items(sys.argv[i]))

    insert_groceries(grocery_dict)


if __name__ == '__main__':
    try:
        read_grocery_file()
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
    finally:
        close_db_connection(CONN)
