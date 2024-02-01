import sys
import random
import string

#I'm too lazy when it come to Check for command line arguments and handle shitty cases :/

def letscountig(str)

    spaces = str.count(' ')
    numbers = sum(1 for char in str if char.isdigit()) 