def is_dna_valid(user_input):

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

    return user_input.upper()