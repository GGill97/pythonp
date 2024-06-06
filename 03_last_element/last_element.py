def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst:
        return lst[-1]

# Add some test calls to print results
print(last_element([1, 2, 3]))  # Expected output: 3
print(last_element([]))  # Expected output: None