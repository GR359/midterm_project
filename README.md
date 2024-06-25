# midterm_project
This is the midterm project for IS601.

# JSON File Processing Script

## Overview
This script processes JSON data from a file containing order details. It generates two separate JSON files: one for customers and another for items. The `customers.json` file maps phone numbers to customer names, ensuring each phone number appears only once. The `items.json` file lists each item, its price, and the number of times it was ordered.

## Features
- Reads data from a JSON file.
- Extracts unique customer information.
- Aggregates item data and counts orders for each item.
- Outputs the data into two structured JSON files.

## Prerequisites
- Python 3.x

## Setup
1. Ensure Python 3.x is installed on your system.
2. Place the script in a project directory.
3. Ensure the JSON file with orders (`example_orders.json`) is placed in the correct directory as specified in the script (`D:\Python\is601\midterm_project`) or you can change the directory according to your configuration.

## Running the Script
To run the script, navigate to the directory containing the script and execute the following command in the terminal:

```bash
python midterm_project.py

