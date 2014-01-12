__author__ = 'Andreas'
import sys

#meal = float(raw_input("How much is the base cost of your meal?"))
#tax = float(raw_input("What is the tax rate?"))
#tip = float(raw_input("What tip do you want to give?"))

meal = float(sys.argv[1])
tip = float(sys.argv[2])
tax = float(sys.argv[3])

tax_value = meal * (tax/100)
meal_with_tax  = meal + tax_value
tip_value = meal_with_tax * (tip/100)

total = meal_with_tax + tip_value

print "The base cost of the meal is " + str(meal)
print "The tax on the meal in dollars is {:.2f}".format(tax_value)
print "The tip you'll be expected to pay is {:.2f}".format(tip_value)
print"The total meal price will be {:.2f}".format(total)