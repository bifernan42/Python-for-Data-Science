import time as tm
import datetime as dt


def format_time():
    time = tm.time()
    today = dt.datetime.now()
    message = "Seconds since January 1, 1970:"
    print(f"{message} {time:,} or {time:.2e} in scientific notation")
    print(today.strftime("%b %d %y"))

format_time()
