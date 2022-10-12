# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    previous_letter = ""
    previous_cost = None
    total_cost = 0
    for letter, cost in zip(S[::-1], C):
        if letter == previous_letter:
            total_cost += previous_cost
        previous_letter = letter
        previous_cost = cost
    return total_cost
