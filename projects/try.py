# try lang mini game, for learning purposes and learning python in general.

import random
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(num)
print("Welcome to the number guessing game!")

num_seq = list(range(50, 4, -5)) # FOR DECREASING ORDER
print(num_seq) # Creating a list from 50 - 5, in reverse, in multiples of 5