# System level imports
import datetime
import logging
import os

from api.s1 import test_logging
from api.s2 import more_testing

# Time and path data for naming the log file
time_now = datetime.datetime.now()
timestamp = time_now.strftime("%Y%m%d-%H%M%S")
path_file_log = os.path.join(os.path.dirname(__file__), f"{timestamp}_use_api_to_clone_log_file.log")  # create the log file in this repo

# Configure base logger settings
formatter_log = logging.Formatter("%(levelname)8s: %(message)s")
formatter_log = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
logger_root = logging.getLogger()
logger_root.setLevel(logging.DEBUG)

# Configure logger for console
loghandler_console = logging.StreamHandler()
loghandler_console.setFormatter(formatter_log)
loghandler_console.setLevel(logging.DEBUG)
logger_root.addHandler(loghandler_console)

# Configure logger for file
loghandler_file = logging.FileHandler(path_file_log)
loghandler_file.setFormatter(formatter_log)
loghandler_file.setLevel(logging.DEBUG)
logger_root.addHandler(loghandler_file)

logging.info("start")

test_logging()
more_testing()

logging.info("end")


def sub(x, y):
    if x == 10:
        print(10)
    return x-y


print("abc")

long_list = ["this", "list", "contains", "too", "many", "elements", "for", "one", "line"]

# # example 1
# def f(myvar):
#     return myva * 2

# # example 2 - ruff - Function definition does not bind loop variable `i`
# def make_three_adders():
#     result = []
#     for i in [10, 20, 30]:
#         def add(x):
#             return x + i
#         result.append(add)
#     return result
# for adder in make_three_adders():
#     print(adder(7))

print(0)
def func():
    print(1)
func()
