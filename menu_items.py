# menu_items Contains:


def menu(input_value = 0 , input_list = [], selection = 0):
    # Displays Menu Items and Prices
    output_list = input_list
    output_bill = input_value
    # menu_categories = ['Appetizer menu', 'Main menu', 'Dessert menu']
    Menu = { 
        "app_menu_dic": {
            "Hand Cut Fries": 8.00,
            "Fried Street Corn": 9.00,
            "Potato Salad": 8.50,
            "Flatbread": 8.00
        },
        "main_menu_dic": {
            "Peperoni Pizza": 12.00,
            "Veggie Pizza": 10.00,
            "Meaty Pizza": 14.00
        },
        "dessert_menu_dic": {
            "Seasonal Ice cream": 6.00,
            "Seasonal slice of Pie": 8.00
    }}
    if selection == 0:
        print(list(Menu.keys()))
        selection = (input("Input a menu category: ")).lower()
    if selection == 'appetizer' or 'main' or 'dessert':
        print(f"So from the {selection} menu pick what you would like")
        selection = f'{selection}_menu_dic'
        print(Menu[selection])
        for key, value in Menu[selection].items():
            loop_state = True
            while loop_state == True:
                user_input=input(f'Would you like {key}? is costs {value}$ \n \
                [Y] yes or [N] no')
                if user_input == 'Y':
                    print(f"You've selected {key}! ")
                    menu_item = key
                    item_amount = int(input(f'How many of {key} would you like'))
                    total_item = item_amount * value
                    print(f"You've entered you want {item_amount} of {menu_item}")
                    output_list.append(menu_item)
                    output_bill.append(item_amount)
                    loop_state = False
                if user_input  == 'N':
                    print("Moving on to the next item")
                    loop_state = False
    else:
        print(f'The selection {selection} doesnt exist yet')
        output_bill, output_list = menu(output_list, output_bill)
        return output_bill, output_list
    return output_bill, output_list

#  the amount of tax,
def tax_select(selection = 0):
    state_tax = 0.10
    if selection == 0:
        print(f'This states tax is {state_tax} ')
        return state_tax
    if selection != 0:
        tax = selection
        if len(tax) <= len(00.00):
            return tax
        if len(tax) <= len(00.0):
            tax = tax / 10
        if len(tax) <= len(00):
            tax = tax / 100
            return
        if len(tax) <= len(0):
            tax = tax / 1000
        else:
            print(f"you input {selection} this is invalid \n \
                keep this input to either a format of a number of X, XX, XX.X, or XX.XX")
            user_in = int(input())
        output = (tax_select(user_in))
        return output

#  and the menu dictionary