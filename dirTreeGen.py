__author__ = 'fernass daoud'


print("**********************************************")
print("******* The Directory Tree Generator *********")
print("\n")
print("**********************************************")

from CommandlineParser import CommandlineParser
from RulesGenerator import RulesGenerator
''' This is a directory tree generator.
Rules for generating the directory tree are stored in an input file'''

# parse commandline and return a commandline object contaqining arguments and options
cmd_obj = CommandlineParser()

print("Input File: ",cmd_obj.args.inputfile)

rules_gen = RulesGenerator(cmd_obj)
rules_gen.generate()
rules_gen.apply()