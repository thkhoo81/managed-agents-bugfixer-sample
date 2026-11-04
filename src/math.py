"""Small math helpers.

Contains one deliberately planted bug so the bug-fixer lab has something
real to reproduce and fix. See tests/test_math.py for the failing case.
"""


def factorial(n):
    """Return n! (the product of every integer from 1 to n).

    factorial(0) is 1 by definition.
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
