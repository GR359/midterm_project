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




