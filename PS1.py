#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Fri Apr 21 20:56:43 2017
    
    @author: anna
    """
#a
#Вартість будинку 1000000
total_coast = float(input("Enter total cost of the house: "))
#річна зп
annual_salary = float(input("Enter your year salary: "))
#зарплата місячна
monthly_salary = annual_salary / 12
#обовязковий платіж
portion_saved = monthly_salary * 0.1
# перший внесок
portion_down_payment = total_coast * 0.25
current_savings = 0
count_month = 0
r = 0.04
while current_savings <= portion_down_payment:
    current_savings = portion_saved + current_savings+current_savings*r/12
    count_month = count_month + 1
print ("Number of months savings: ", count_month)

#b
portion_down_payment = 0.25
current_savings = 0.0
rate = 0.04
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))
semi_annual_raise = float(input("The semi-annual raise: "))
down_payment_needed = total_cost * portion_down_payment
no_months_saved = 0
previous_savings = 0.0
monthly_savings = annual_salary / 12 * portion_saved

while current_savings < down_payment_needed:
    if no_months_saved == 0:
        # If it is month 0, there is no investment return, just the monthly savings
        current_savings = monthly_savings
    else:
        # Check if time for semi-annual raise, if so re-calculate
        # annual_salary and monthly_savings
        
        if no_months_saved % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_savings = annual_salary / 12 * portion_saved
        
        current_savings = (previous_savings * (1 + (rate / 12))) + monthly_savings
no_months_saved += 1
    previous_savings = current_savings

print("Number of months saved: ", no_months_saved)
print("Current savings: ", current_savings)

#c
portion_down_payment = 0.25
current_savings = 0.0
rate = 0.04
annual_salary_input = float(input("The starting annual salary: "))
annual_salary = annual_salary_input
portion_saved = 0.0
total_cost = 1000000
semi_annual_raise = 0.07
down_payment_needed = total_cost * portion_down_payment
no_months_saved = 0
previous_savings = 0.0
num_guesses = 0
low = 0
high = 10000
guess = (high + low)/2.0
current_guess = guess / 10000
guessed = False
monthly_savings = annual_salary / 12 * current_guess
num_guesses = 0

while not guessed:
    num_guesses += 1
    while current_savings < down_payment_needed:
        if no_months_saved == 0:
            # If it is month 0, there is no investment return, just the monthly savings
            current_savings = monthly_savings
        else:
            # Check if time for semi-annual raise, if so re-calculate
            # annual_salary and monthly_savings
            
            if no_months_saved % 6 == 0:
                annual_salary *= 1 + semi_annual_raise
                monthly_savings = annual_salary / 12 * current_guess
            current_savings = (previous_savings * (1 + rate / 12)) + monthly_savings

no_months_saved += 1
    previous_savings = current_savings
    
    # Check to see if new guess is close to original high, if so, it is not
    # possible to pay down the down payment in 36 months with the given salary
    if current_guess >= .99:
        break

if no_months_saved > 36:
    # Guess was too low, choose between guess and 10000
    # Reset required var's
    low = guess
    elif no_months_saved < 36:
        # Guess was too high, choose between 0 and guess
        # Reset required var's
        high = guess
else:
    # Guessed in 36 months, check that the diff was $100 or less
    if current_savings - down_payment_needed <= 100:
        guessed = True
        else:
            high = guess

no_months_saved = 0
    previous_savings = 0.0
    current_savings = 0.0
    annual_salary = annual_salary_input
    guess = (high + low)/2.0
    current_guess = guess / 10000
    monthly_savings = annual_salary / 12 * current_guess


if current_guess >= .99:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Number of guesses: ", num_guesses)
    print("Best savings rate: ", current_guess)
