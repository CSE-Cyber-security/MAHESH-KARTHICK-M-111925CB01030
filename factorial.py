"""
Factorial Module

This module provides functions to calculate factorials using both
iterative and recursive approaches.
"""

import math


def factorial_iterative(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using an iterative approach.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using a recursive approach.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    num = 5
    print(f"Iterative factorial of {num}: {factorial_iterative(num)}")
    print(f"Recursive factorial of {num}: {factorial_recursive(num)}")
    print(f"Built-in math module factorial of {num}: {math.factorial(num)}")
