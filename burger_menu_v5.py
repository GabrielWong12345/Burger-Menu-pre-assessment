"""
Burger Combo Menu 
v5 - Search/Edit
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
    # Formats the dictionary into a readable string for EasyGui
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
        # Component 3
        elif selection == "View Menu":
            display_menu(current_menu)
            
        # Component 4: Add Combo
        elif selection == "Add Combo":
            new_name = easygui.enterbox("Enter the name of the new combo:", "Add Combo")
            
            if new_name:
                new_items = easygui.enterbox(f"Enter the items for {new_name}:", "Add Items")
                
                try:
                    new_price = float(easygui.enterbox(f"Enter the price for {new_name}:", "Add Price"))
                    current_menu[new_name] = [new_price, new_items]
                    easygui.msgbox(f"{new_name} has been added.")
                except:
                    easygui.msgbox("Invalid price. Combo not added.")

        # Component 5: Search/Edit
        elif selection == "Search/Edit":
            search_name = easygui.enterbox("Enter the name of the combo to find/edit:", "Search/Edit")
            
            if search_name:
                # Making it case-insensitive for search
                search_key = search_name.title()
                
                if search_key in current_menu:
                    details = current_menu[search_key]
                    info = f"CURRENT DETAILS:\nItems: {details[1]}\nPrice: ${details[0]:.2f}\n\nDo you want to edit this combo?"
                    
                    edit_choice = easygui.buttonbox(info, "Combo Found", ["Edit Price", "Edit Items", "No (Back)"])
                    
                    if edit_choice == "Edit Price":
                        try:
                            new_p = float(easygui.enterbox(f"New price for {search_key}:", "Edit Price"))
                            current_menu[search_key][0] = new_p
                            easygui.msgbox(f"Price updated to ${new_p:.2f}")
                        except:
                            easygui.msgbox("Invalid price. No changes made.")
                            
                    elif edit_choice == "Edit Items":
                        new_i = easygui.enterbox(f"New items for {search_key}:", "Edit Items")
                        if new_i:
                            current_menu[search_key][1] = new_i
                            easygui.msgbox("Items updated.")
                else:
                    easygui.msgbox(f"'{search_name}' was not found.")

        elif selection == "Delete":
            easygui.msgbox("You selected: Delete ")

        elif selection == "Output All":
            print("\n--- Current Menu ---")
            for name, details in current_menu.items():
                print(f"{name}: {details[1]} - ${details[0]:.2f}")
            easygui.msgbox("Full menu printed to the console.")