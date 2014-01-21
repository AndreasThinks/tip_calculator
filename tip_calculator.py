__author__ = 'Andreas'
import sys
from optparse import OptionParser
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

try:
    meal = float(sys.argv[1])
except ValueError:
    print ("Please enter an int or float")
    meal = float(raw_input("Please enter a better value here  "))
try:
    tip = float(sys.argv[2])
except ValueError:
    print ("Please enter an int or float")
    tip  = float(raw_input("Please enter a better value here  "))

try:
    tax = float(sys.argv[3])
except ValueError:
    print ("Please enter an int or float")
    tax = float(raw_input("Please enter a better value here  "))

try:
    inverse = 1.0 / meal
except ValueError:
    print ("Meal should be a int or float")
    meal = float(raw_input("Please enter a better value here  "))

try:
    inverse = 1.0 / tip
except ValueError:
    print ("Meal should be a int or float")
    tip = float(raw_input("Please enter a better value here  "))

try:
    inverse = 1.0 / tax
except ValueError:
    print ("Meal should be a int or float")
    tax = float(raw_input("Please enter a better value here  "))

#parser = OptionParser()

#parser.add_option("-f", "--first", dest="meal", help = "The price of your meal", type = "float")
#parser.add_option("-s", "--second", dest="tip", help = "The tip percent", type = "float", default = 10.00)
#parser.add_option("-t", "--third", dest="tax", help = "The tax percent", type = "float", default = 7.5)

#(options, args) = parser.parse_args()

#if not (options.meal):
 #   parser.error("You need to supply a meal price")

def main():
    tax_value = meal * (tax/100)
    meal_with_tax  = meal + tax_value
    tip_value = meal_with_tax * (tip/100)
    total = meal_with_tax + tip_value
    #except ValueError:
     #   print "meal values must be a value (duh)"
      #  meal = float(raw_input("Please input your meal value"))

    print "The base cost of the meal is " + str(meal)
    print "The tax on the meal in dollars is {:.2f}".format(tax_value)
    print "The tip you'll be expected to pay is {:.2f}".format(tip_value)
    print"The total meal price will be {:.2f}".format(total)

main()