"""
Burger Combo Menu 
v3 - View Menu
Created by Gabriel Wong
"""

import easygui

def setup_menu():
    # [Combo name] : [Price, "Description of items in the combo"]
    burger_menu = {
        "Value": [10.50, "Beef burger, Fries, Fizzy drink"],
        "Cheezy": [11.50, "Cheeseburger, Fries, Fizzy drink"],
        "Super": [15.00, "Cheeseburger, Large fries, Smoothie"]
    }
    return burger_menu
# Component 3: View Menu
def display_menu(menu):
    """Formats the dictionary into a readable string for EasyGui"""
    menu_string = ""
    for name, details in menu.items():
        menu_string += f"COMBO: {name.upper()}\nItems: {details[1]}\nPrice: ${details[0]:.2f}\n\n"
    
    easygui.msgbox(menu_string, "Current Burger Menu")

# MAIN LOOP
if __name__ == "__main__":
    current_menu = setup_menu()
    
    # Component  2: Main Menu Loop
    run_program = True
    while run_program:
        
        msg = "Welcome to the Burger Combo System. Please select an option:"
        title = "Main Menu"
        choices = ["View Menu", "Add Combo", "Search/Edit", "Delete", "Output All", "Exit"]
        
        selection = easygui.buttonbox(msg, title, choices)

        if selection == "Exit" or selection is None:
            easygui.msgbox("Program closing. Goodbye!")
            run_program = False
        
        elif selection == "View Menu":
            # Component 3
            display_menu(current_menu)
            
        elif selection == "Add Combo":
            easygui.msgbox("You selected: Add Combo")

        elif selection == "Search/Edit":
            easygui.msgbox("You selected: Search/Edit")

        elif selection == "Delete":
            easygui.msgbox("You selected: Delete ")

        elif selection == "Output All":
            # Component 7: Output All
            print("\n--- Current Menu ---")
            for name, details in current_menu.items():
                print(f"{name}: {details[1]} - ${details[0]:.2f}")
            easygui.msgbox("Full menu printed to the console.")