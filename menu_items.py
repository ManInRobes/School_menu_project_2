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
        selection = (input("Input a menu selection: ")).lower()
    if selection == 'appetizer' or 'main' or 'dessert':
        print(f"So from the {selection} menu pick what you would like")
        selection = f'{selection}_menu_dic'
        for key, value in Menu[selection].items():
            print(key, value)

            # If input matches key than confirm,
            # add insert to list logic
            # add value of the key selected to a list
            # if key is selected append key to output_list and add value of key to value_add
            # else try it again
            #
            # -output_price = output_price
            # -output_list = output_list
            # if user wants to add more things to the list then run the function with the input of the list then bill
            # -return output_bill, output_list
    else:
        print(f'The selection {selection} doesnt exist yet')
        output_bill, output_list = menu(output_list, output_bill)
        return output_bill, output_list

printed = menu()
print(printed)


# #  the amount of tax,
# def tax_select(selection = 0):
#     state_tax = 0.10
#     if selection == 0:
#         print(f'This states tax is {state_tax} ')
#         return state_tax
#     if selection != 0:
#         tax = selection
#         if len(tax) <= len(00.00):
#             return tax
#         if len(tax) <= len(00):
#             tax = tax / 100
#             return
#         else:
#             print(f"you input {selection} this is invalid \n \
#                 keep this input to either a format of a number of XX or XX.XX")
#             user_in = int(input())
#         output = (tax_select(user_in))
#         return output

# #  and the menu dictionary