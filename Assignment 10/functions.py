# functions.py
import math

def add_and_sort_numbers(num1, num2=math.pi, verbose=False):
    # Calculate the sum
    total = num1 + num2

    # Create a sorted list containing both numbers
    sorted_list = [num1, num2]
    sorted_list.sort()

    if verbose:
        print("Parameters:")
        print(f"num1 = {num1}")
        print(f"num2 = {num2}")
        print("Results:")
        print(f"Sum: {total}")
        print(f"Sorted List: {sorted_list}")

    return total, sorted_list

