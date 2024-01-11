def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

str = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
find_needle(str)