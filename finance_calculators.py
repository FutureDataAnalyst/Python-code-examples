# This is a program that allows the user to access two different financial calculators:
# 1) investment calculator - to calculate interest on an ivestment
# 2) home loan repayment calculator - calculates the amount to be repaid on a home loan each month

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if (user_choice.lower() == "investment"):
    print("Thank you for choosing investment.")

# 'P' is the amount that the user deposits
# 't' is the number of years that the money is being invested
# 'r' is the interest rate entered below divided by 100
# 'A' is the total amount once the interest has been applied

    P = int(input("How much money are you depositing?: "))

    interest_rate = int(input("What is your interest rate value? (Enter the number only): "))

    r = ((interest_rate)/100)
    print("Your interest rate value is: ", r)

    t = int(input("How many years are you planning to invest?: "))

    A = P * math.pow((1+r),t)
    print("The total amount once the interest rate has been applied: ", A)

    interest = input("Please choose which interest you would like, 'simple' or 'compound'?: ")


    # Simple interest formula
    simple_interest = A = P*(1 + r*t)
    
    # Compound interest formula
    compound_interest = A = P * math.pow((1+r),t)

    
    if (interest.lower() == "simple"):
        print("Simple interest is: ", simple_interest)
    

    elif (interest.lower() == "compound"):
        print("Compound interest is: ", compound_interest)
    

    else:
        print("Please try again and choose either 'simple or 'compound'. ")



elif (user_choice.lower() == "bond"):
    
    print("Thank you for choosing bond option.")
    # 'P' is the present value of the house
    # 'i' is the monthly interest rate
    # 'n' is the number of months over which the bond will be repaid


    P = int(input("Enter present value of the house, e.g. 100000: "))

    interest_rateB = int(input("Enter interest rate without decimals e.g. 7: "))

    n = int(input("Enter the total number of months planned to repay the bond, e.g. 120: "))

    i = ((interest_rateB)/100)/12
    print("Your monthly interest rate: ", i)


    # Bond repayment formula
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("Your monthly repayment: ", repayment)


else:
    print("Invalid entry. Please try again.")