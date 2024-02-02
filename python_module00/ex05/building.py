import sys
import random
import string

#I'm too lazy when it come to Check for command line arguments and handle shitty cases :/

def letscountig(str):

    text = sum(1 for char in str)
    spaces = str.count(' ')
    numbers = sum(1 for char in str if char.isdigit())
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    punctuation = sum(1 for char in str if char in string.punctuation)

    print(f"The text contain {text} characters")
    print(f"uppercase  : {upper}")
    print(f"Lowercase  : {lower}")
    print(f"Numbers    : {numbers}")
    print(f"punctuation: {punctuation}")
    print(f"Spaces     : {spaces}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise AssertionError("Only one argument :)")
    if len(sys.argv) == 2:
        result = sys.argv[1]
    else:
        result = print("Enetr a string ")
    
    letscountig(result)

