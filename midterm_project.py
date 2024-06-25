import json
import sys

def read_json(file_name):
#Read the JSON file.
    with open(file_name, 'r') as file:
        return json.load(file)
    
def create_customers_json(orders):
#Creating the customers.json file.
    customers = {}
    for order in orders:
        phone = order['phone']
        name = order['name']
        if phone not in customers:
            customers[phone] = name
    return customers

def create_items_json(orders):
#Creating the items.json file.
    items = {}
    for order in orders:
        for item in order['items']:
            item_name = item['name']
            price = item['price']
            if item_name not in items:
                items[item_name] = {"price": price, "orders": 0}
            items[item_name]["orders"] += 1
    return items

orders_file = "example_orders.json"

# Read the orders from the JSON file
orders = read_json(orders_file)

# Create customers.json
customers = create_customers_json(orders)
with open('customers.json', 'w') as file:
    json.dump(customers, file, indent=4)

# Create items.json
items = create_items_json(orders)
with open('items.json', 'w') as file:
    json.dump(items, file, indent=4)

    print("Files created successfully.")



