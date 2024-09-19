""" 
Find Pi to the Nth digit
This program generate Pi up to n decimal places, where n is the number input by user.
n must be in range 0 to 20.

"""
import math

max_lmt = 20

# Prompt the user for the number of decimal places
while True:
    try:
        p = int(input(f"Enter the number of decimal places up to {max_lmt}: "))

        # Check if the input is within the allowed range
        if 0 <= p <= max_lmt:
            print(f'PI = {math.pi:.{p}f}')
            break
        else:
            print(f"Please enter a number between 0 and {max_lmt}.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
