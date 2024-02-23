# number_queue.py
# program that queues 10 random numbers and takes out one
#   at a time and prints remaining numbers in queue
# author: eoghan walsh

import random

number_queue = []
from_range = 1
to_range = 101
length_of_queue = 10

while len(number_queue) < length_of_queue:
    number_queue.append(random.randint(from_range, to_range))

print(f"queue is {number_queue}")

while len(number_queue) > 0:
    current_number = number_queue.pop(0)
    print(f"current number is {current_number} and the queue is {number_queue}")

print("the queue is now empty")

