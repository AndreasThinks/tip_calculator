__author__ = 'Andreas'
import sys
from optparse import OptionParser

#meal = float(raw_input("How much is the base cost of your meal?"))
#tax = float(raw_input("What is the tax rate?"))
#tip = float(raw_input("What tip do you want to give?"))

#meal = float(sys.argv[1])
#tip = float(sys.argv[2])
#tax = float(sys.argv[3])

parser = OptionParser()

parser.add_option("-f", "--first", dest="meal", help = "The price of your meal", type = "float")
parser.add_option("-s", "--second", dest="tip", help = "The tip percent", type = "float", default = 10.00)
parser.add_option("-t", "--third", dest="tax", help = "The tax percent", type = "float", default = 7.5)

(options, args) = parser.parse_args()

if not (options.meal):
    parser.error("You need to supply a meal price")

tax_value = options.meal * (options.tax/100)
meal_with_tax  = options.meal + tax_value
tip_value = meal_with_tax * (options.tip/100)

total = meal_with_tax + tip_value

print "The base cost of the meal is " + str(options.meal)
print "The tax on the meal in dollars is {:.2f}".format(tax_value)
print "The tip you'll be expected to pay is {:.2f}".format(tip_value)
print"The total meal price will be {:.2f}".format(total)