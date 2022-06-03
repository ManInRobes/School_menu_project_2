import menu_functions as mf
import menu_items as mi

# Personal addition: Calculator add up the bill
def bill_calc(value_list, tax, tip):
    menu_total = sum(value_list)
    tax_amount = tax
    tip_amount = tip
    out = menu_total + tax_amount + tip_amount
    return out
# menu_main contains:
true_state = True
while true_state == True:
    # If you want to continue using the menu functionality:
    usage_state = 0
    if usage_state == 0:
        menu_bill, tax = mf.items_grouping()
        tip = mf.tip_choice
        output = bill_calc(menu_bill, tax, tip)
        print(f"The total of your bill before tax is {menu_bill}$ with a tip of {tip}$ your total comes out to {output}$")
    if usage_state == 1:
        true_state = False
    # If you don't want to quit the menu

# The main body of the code