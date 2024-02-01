
import sys

def letsevenodd(number):
    if number % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
            letsevenodd(num)
        except ValueError:
            print("I only accept integers :)")
    else:
        print("AssertionError: more than one argument is provided")