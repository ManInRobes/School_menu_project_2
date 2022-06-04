import menu_functions as mf
import menu_items as mi

# Personal addition: Calculator add up the bill
def bill_calc(value_list, tax, tip):
    menu_total = sum(value_list)
    out = (menu_total*tax) + (menu_total*tip) + menu_total
    return out


# menu_main contains:
true_state = True
while true_state == True:
    # If you want to continue using the menu functionality:
    usage_state = 0
    if usage_state == 0:
        menu_bill, menu_list, tax = mf.items_grouping()
        tip = mf.tip_choice()
        output = bill_calc(menu_bill, tax, tip)
        print(f"you ordered {menu_list} ")
        print(f"The total of your bill before tax and tip is {sum(menu_bill)}$, tax of {tax} with a tip of {tip}$ and a total that comes out to {output}$")
        user_input = input("would you like to simulate another menu selection? \n \
            [Y] or [N]: ").lower()
        if user_input == "y":
            menu_bill = []
            menu_list = []
        if user_input == "n":
            usage_state == 1
            break
    if usage_state == 1:
        true_state = False
        break
    # If you don't want to quit the menu

# The main body of the code