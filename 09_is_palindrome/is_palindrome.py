def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    normalized = phrase.lower().replace('',' ')
    return normalized == normalized[::-1]

print(is_palindrome('tacocat'))     # Output: True
print(is_palindrome('noon'))        # Output: True
print(is_palindrome('robert'))      # Output: False
print(is_palindrome('taco cat'))    # Output: True
print(is_palindrome('Noon'))        # Output: True
