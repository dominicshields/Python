def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
print(new_inventory.get('strawberries',0))

add_fruit(new_inventory, 'strawberries', 25)
print(new_inventory.get('strawberries',0))