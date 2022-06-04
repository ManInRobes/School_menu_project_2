import menu_items as mi
# menu_functions: Holds two functions,

# One function; displays the items in a grouping,
def items_grouping(menu_bill = [], menu_list = []):
    menus = menu_list
    bills = menu_bill
    while_loop = True
    while while_loop == True:
        bills, menus = mi.menu(bills, menus)
        user_input = input("Are you done making selections from the menu, [Y] or [N]").lower()
        if user_input == "y":
            break
        elif user_input == "n":
            while_loop == True
        else:
            print(f"your input, {user_input} wasn't a valid input try again")
    tax = mi.tax_select()
    return bills, menus, tax
# The second function
def tip_choice():
# Displays the tip options and prompts the user to input a tip
    tip_choices = ['10% [1]', '15% [2]', '20% [3]']
    loop_state = True
    while loop_state == True:
        user_input = int(input(f'please input of the options \n {tip_choices[0]} \n {tip_choices[1]} \n {tip_choices[2]} '))
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