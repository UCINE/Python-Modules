import time
from datetime import datetime

today = datetime.now()

thisformat = today.strftime("%b %d %Y")
def format_time():
    seconds = time.time()

    print(f"Seconds since January 1, 1970: {seconds} or {seconds:.2e} in scientific notation")

format_time()
print(thisformat)