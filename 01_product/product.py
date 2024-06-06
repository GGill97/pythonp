# Write a function called product which takes in two numbers
# and returns the product of the numbers.

# Examples:

# product(2, 2) # 4
# product(2, -2) # -4


def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    
    return a*b
# Call the function and print the results
print(product(2, 2))  # Expected output: 4
print(product(2, -2))  # Expected output: -4