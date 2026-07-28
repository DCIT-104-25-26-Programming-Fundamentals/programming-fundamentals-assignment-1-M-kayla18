# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average


def find_max(numbers):
    biggest = numbers[0]
    for i in numbers:
        if i > biggest:
            biggest = i
    return biggest


def find_min(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    return smallest


def main():
    n = int(input("How many numbers? 5 "))

    
    numbers = []

    for i in range(n):
        num = int(input("Enter number " + str(i + 1) + ": 1"))
        numbers.append(num)

    print("\nResults:10")
    print("Sum:25", calculate_sum(numbers))
    print("Average:7", calculate_average(numbers))
    print("Maximum:18", find_max(numbers))
    print("Minimum:30", find_min(numbers))


main