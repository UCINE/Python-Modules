import time

def format_time():
    seconds = time.time()

    print(f"Seconds since January 1, 1970: {seconds} or {seconds:.2e} in scientific notation")

format_time()