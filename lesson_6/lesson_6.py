# Декомпозиция - разделение кода по модулям

"""
Кастомные модули : lesson_1.py, result.py, test.py
"""

"""
Встроенные модули : random, math, datetime, time
"""


"random:"
# import random 

# num_list = (1,2,3,4,5)

# print(random.choice(num_list))

# from random import randint

# num = randint(1,10)
# print(num)

# from random import *

# num = randint(1,10)
# print(num)

# print(choice(num_list))

"time"

import time

# print("Код запуститься через 5 сек")

# time.sleep(5)

# print("Код запустился")

# time_start = time.time()

# n = 0
# while 5 > n:
#     n += 1
#     # time.sleep(1.5)
#     print("Loading..")

# time_end = time.time()

# result = time_end - time_start
# print(result)


"""
Внещние модули : 
"""

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)

cprint("Hello, Nurai!", "blue", "on_green")

