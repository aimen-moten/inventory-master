# Product Inventory Management System

This Python project is a simple yet effective implementation of a Product Inventory Management System. It provides classes and functions to manage products and inventory efficiently.

## Features

- **Product Class**: The `Product` class represents a product in the inventory. It includes properties for name, value, amount, and scale (e.g., 'kg'). Each product is assigned a unique ID.

- **Inventory Class**: The `Inventory` class manages multiple products. It allows you to add products to the inventory and provides properties to retrieve information about the inventory, such as total product value, total product count, and the count of different products.

- **Object Factories**: The `ObjFactory` abstract class serves as the base class for object factories, providing a common interface for creating objects. Concrete implementations `ProductFactory` and `InventoryFactory` allow you to create multiple product or inventory instances easily.

## Usage

Here's how you can use this project:

1. Create an inventory instance using `Inventory()`.

2. Add products to the inventory using the `product_add` method, either one by one or in batches.

3. Retrieve information about the inventory, such as the total value, total count, and count of different products.

## Example

```python
# Create an inventory
inventory = Inventory()

# Add some products to the inventory
gen_prod = lambda value: Product(value=value)
for i in range(1, 10):
    inventory.product_add(gen_prod(value=i))
for i in range(1, 5):
    inventory.product_add(gen_prod(value=i))

# Get amount of product on hand, value of product, and amount of different products
prod_amt = inventory.product_count
prod_val = inventory.product_value
prod_diff = inventory.product_diff_amount

# Print the results
for name, info in (("amount of product", prod_amt), ("value of product", prod_val), ("different products", prod_diff)):
    print(f"{name}: {info}")
    
# Print details of each product in the inventory
for product in inventory.products:
    print(f"{product} details: {inventory.products[product]}")
