def truncate(text, number_of_letters):
    """
    Returns a truncated version of the input string, cutting it off at n characters. 
    If the string exceeds n characters, the output ends with "..." 
    unless n is less than or equal to 3, in which case only the first n characters are returned without ellipsis. 
    If n is zero or negative, returns an empty string. 
    Special cases such as unicode and newline characters are handled as regular characters, and the function expects a string as input
    
    """
    if number_of_letters <= 0:
        return ''
    
    if len(text) <= number_of_letters:
        return text
    
    if number_of_letters <= 3:

        return text[:number_of_letters]

    words = text.split()
    output = ''
    for word in words:
        if output:
            if len(output) + 1 + len(word) + 3 > number_of_letters:
                return output + '...'
            output += ' ' + word
        else:
            if len(word) + 3 > number_of_letters:
                return word[:number_of_letters - 3] + '...'
            output = word

    return output
