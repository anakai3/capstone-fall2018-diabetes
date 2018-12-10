class GroceryItem(object):
    def __init__(self, brand_name, item_name, quantity, unit):
        self.brand_name = brand_name
        self.item_name = item_name
        self.quantity = quantity
        self.unit = unit


def get_grocery_item(item):
    # item is in the form brand_name,item_name,quantity,unit
    if not item:
        return None

    item_parts = item.split(",")
    brand_name = item_parts[0].strip()
    item_name = item_parts[1].strip()
    quantity_unit = item_parts[2].strip().split()
    quantity = float(quantity_unit[0]) if quantity_unit[0] else 0.0
    unit = quantity_unit[1] if quantity_unit[1] else 'g'

    return GroceryItem(brand_name, item_name, quantity, unit)


def get_grocery_list_items(file_path):
    if not file_path:
        return None
    grocery_items = []
    with open(file_path, 'r') as glfile:
        for item in glfile:
            grocery_item = get_grocery_item(item)
            if not grocery_item:
                continue
            grocery_items.append(grocery_item)

    return grocery_items
