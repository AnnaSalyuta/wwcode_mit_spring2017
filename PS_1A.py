total_coast = float(input("Enter total cost of the house: "))
annual_salary = float(input("Enter your year salary: "))
monthly_salary = annual_salary / 12
portion_saved = monthly_salary * 0.1
portion_down_payment = total_coast * 0.25
current_savings = 0
count_month = 0
r = 0.04
while current_savings <= portion_down_payment:
    current_savings = portion_saved + current_savings+current_savings*r/12
    count_month = count_month + 1
print ("Number of months savings: ", count_month)
