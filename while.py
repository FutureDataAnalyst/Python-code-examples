# This is a program that asks for user input to enter a number
# When the user enters -1, the program will stop requesting for another number
# After that happens, the program will calculate the sum and average of the numbers entered, excluding -1
# number_ofEntries counts how many times the user entered the number, except the break condition "-1"
# sum is the total value of entered numbers
# n is a number entered by the user

import math


number_ofEntries = 0

sum = 0

n = int(input("Please enter a number (-1 to exit): "))


while n != -1:
    
    number_ofEntries += 1

    sum += n

    average = sum / number_ofEntries

    n = int(input("Please enter a number (-1 to exit): "))
    
    
    if n == -1:
        
        print("Sum = ", sum)
        
        print("Average = ", average)
       
        break
    