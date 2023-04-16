'''
Created on Sep 8, 2022

@author: Brandon Demeritt
'''

#get amounts from user
print("Please enter the amounts needed for lemonade.")
cupsLemonJuice = float(input("Enter the amount of lemon juice needed(in cups): \n"))
cupsWater = float(input("Enter the amount of water needed(in cups):\n"))
cupsAgave = float(input("Enter the amount of Agave Nectar needed(in cups): \n"))
servingSize = float(input("Enter how many servings this makes: \n"))

#print amounts
print("\nLemonade ingredients - yields", servingSize, "servings")
print(cupsLemonJuice, "cups of Lemon Juice.")
print(cupsWater, "cups of water.")
print(cupsAgave, "cups of Agave Nectar.\n")

#Get desired serving size from user
desiredServing = float(input("How many servings do you want to make? \n"))

#calculate difference from serving size
servingDifference = desiredServing / servingSize

#display amounts needed for desired serving size
print("\nLemonade ingredients for", desiredServing, "servings.")
print(cupsLemonJuice * servingDifference, "cups of Lemon Juice.")
print(cupsWater * servingDifference, "cups of water.")
print(cupsAgave * servingDifference, "cups of Agave Nectar.\n")

#calculate cups to gallons for each ingredient and print
print("Lemonade ingredients - yields", desiredServing, "servings")
print(cupsLemonJuice * servingDifference / 16, "gallon(s) of lemon juice.")
print(cupsWater * servingDifference / 16, "gallon(s) of water.")
print(cupsAgave * servingDifference / 16, "gallon(s) of agave nectar.")

print("\nThe End")
