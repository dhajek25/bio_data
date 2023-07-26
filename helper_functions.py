def is_dna_valid(user_input):
    """
    Checks if the provided DNA sequence contains only valid nucleotides (A, C, T, G).

    Parameters:
    - user_input (str): The DNA sequence provided by the user.

    Returns:
    - list: A list of invalid characters found in the input. If the list is empty, the sequence is valid.
    """


    valid_letters = ['A', 'C', 'T', 'G']
    is_invalid_letters = []

#    if user_input == '':
#        error_message = "Empty input! Please provide a valid DNA sequence."
#        return error_message

    for char in user_input:
        if char not in valid_letters:
            is_invalid_letters.append(char)
    return is_invalid_letters

def upper_letters(user_input):
    """
    Converts the provided input string to uppercase.

    Parameters:
    - user_input (str): The string to be converted to uppercase.

    Returns:
    - str: The input string in uppercase.
    """
    return user_input.upper()