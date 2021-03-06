# menu_items Contains:


def menu(input_value = [] , input_list = [], selection = 0):
    # Displays Menu Items and Prices
    output_list = input_list
    output_bill = input_value
    if input_list == []:
        print("you currently have nothing in your 'cart' ")
    if input_list != []:
        print(f"you currently have the following items: {input_list} in your 'cart' "  )
        print(f"Also your current bill is {sum(input_value)}$")
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
                    [Y] yes or [N] no: ')
                    if user_input == 'Y':
                        print(f"You've selected {key}! ")
                        menu_item = key
                        item_amount = float(input(f'How many of {key} would you like: '))
                        total_item = item_amount * value
                        print(f"You've entered you want {item_amount} of {menu_item}")
                        output_list.append(f"{item_amount}, {menu_item}")
                        output_bill.append(item_amount)
                        loop_state = False
                    if user_input  == 'N':
                        print("Moving on to the next item")
                        loop_state = False
        else:
            print(f'The selection {selection} doesnt exist yet')
            output_bill, output_list = menu(output_bill, output_list)
            return output_bill, output_list
        return output_bill, output_list


#  the amount of tax, This is my least favorite part of my code but the only way I could think of doing it at the time
def tax_select(selection = 0):
    if selection == 0:
        selection = float(input("you can input a custom value one number (ie. 1 is 1%, 10 is 10%, and 100 is 100%): "))
    if selection != 0:
        tax = selection
        return tax

    else:
        print(f"you input {selection} this is invalid \n \
            keep this input to either a format of a number of X, XX, XX.X, or XX.XX")
        user_in = tax_select()
        return user_in
    output = (tax_select(user_in))
    return output

#  and the menu dictionary