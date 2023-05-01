name = input("Please enter your full name: ")

# to check the number of characters in the string I will assign it to a variable x and use len function
x = len(name)

# if the number of characters entered equals zero, then the message below will be printed
if x == 0 :
    print ("You haven't entered anything. Please enter your full name.")

# else if the number of characters entered is less than 4, the following message will be printed
elif x < 4 :
    print ("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

# else if the number of characters entered is more than 25, the following message will be printed
elif x > 25 :
    print ("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# in any other case print the following message
else :
    print ("Thank you for entering your name.")
