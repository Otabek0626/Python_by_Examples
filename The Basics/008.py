#Ask for the total price of the bill, then ask how
#many diners there are. Divide the total bill by the
#number of diners and show how much each
#person must pay
price = int(input("How much total price of the bill? "))
people = int(input("How many diners there are? "))
per_people = price / people
print("Each person must pay",per_people)
