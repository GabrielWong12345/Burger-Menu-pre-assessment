"""
Burger Combo Menu 
v1 - Setup Data Structure
Created by Gabriel Wong
"""

def setup_menu():
    # [Combo name] : [Price, "Description of items in the combo"]
    burger_menu = {
        "Value": [10.50, "Beef burger, Fries, Fizzy drink"],
        "Cheezy": [11.50, "Cheeseburger, Fries, Fizzy drink"],
        "Super": [15.00, "Cheeseburger, Large fries, Smoothie"]
    }
    return burger_menu

# MAIN LOOP
if __name__ == "__main__":
    
    current_menu = setup_menu()
    
    # Test print to ensure data is loaded correctly
    print("--- Initial Burger Menu Loaded ---")
    for name, details in current_menu.items():
        price = details[0]
        items = details[1]
        print(f"Combo: {name} | Items: {items} | Price: ${price:.2f}")