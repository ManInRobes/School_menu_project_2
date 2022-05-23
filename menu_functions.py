import menu_items as mi
# menu_functions: Holds two functions,

# One function; displays the items in a grouping,
def items_grouping():
    menu_bill, menu_list = mi.menu
    tax = mi.tax()
    return menu_bill, menu_list, tax
# Prompts the user to select an item,

# Returns the item name and price,

# The second function
def tip_choice():
# Displays the tip options and prompts the user to input a tip
    tip_choices = ['10% [1]', '15% [2]', '20% [3]']
    loop_state = True
    while loop_state == True:
        user_input = int(input('please input of the options \n [1] \n [2] \n [3] '))
        if user_input == 1 or 2 or 3:
            if user_input == 1:
                tip = .10
                return tip
            if user_input == 2:
                tip = .15
                return tip
            if user_input == 3:
                tip = .20
                return tip
        else:
            print(f"You input {user_input} this is invalid please try another.")