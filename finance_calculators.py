import math

while True:
# Prompt the user to choose between the two calculators, bond or investment. Use .lower() to ensure no case-sensitivity
    finance_type = input("Welcome to finance calculator! To begin, please choose your calculation from either 'bond' or 'investment': ").lower()

# Check if the user entered a valid choice
    if finance_type in ["investment", "bond"]:
        break
    else:
        print("Invalid finance type. Please choose 'bond' or 'investment'.")

# An if loop for bond and investment calculators
if finance_type == "investment":
    print("You have chosen: investment")
    deposit = float(input("Enter the amount of your deposit: "))
    interest = float(input("Enter your interest: "))
    years = float(input("Enter the number of years you plan on investing: "))
    investment_type = input("Choose your investment type: 'compound' or 'simple': ").lower()

    P = deposit
    t = years
    r = interest / 100
# A nested if statement, dependent on investment type
    if investment_type == "simple":
        total_sum = P * (1 + r * t)
        print(f"Your total after {years} years of investment would be {total_sum}")

    elif investment_type == "compound":
        total_sum = P * math.pow((1 + r), t)
        print(f"Your total after {years} years of investment would be {total_sum}")

    else:
        print("Invalid investment type. Please choose 'compound' or 'simple'.")

elif finance_type == "bond":
    print("You have chosen: bond")
    house_value = float(input("Enter the starting house value: "))
    interest_rate = float(input("Enter the interest rate value: "))
    repayment_months = int(input("Enter the number of months of the bond repayment: "))
    P = house_value
    i = interest_rate / 100
    n = repayment_months
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"This is your repayment total: {repayment}")

# If the user inputs anything other than bond or investment, prompt them to choose again.
else:
    print("Invalid finance type. Please choose 'bond' or 'investment'.")