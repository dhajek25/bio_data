s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def dna_nucleotides_count(s):
    """ Count the nucleotides (A, T, C, G) in the input string.

    Parameters:
    s (str): The input string to count nucleotides in.
    
    Returns:
    A view object of the dictionary's items. Each item is a tuple with a nucleotide and its count.
    
    Example:
    dna_nucleotides_count('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    dict_items([('A', 20), ('T', 21), ('C', 12), ('G', 17)])
    """

    nucl_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for e in s:
        if e in nucl_dict.keys():
            nucl_dict[e] += 1

    return nucl_dict

def transcription(s):
    return s.replace('T', 'U')

def complement(s):

    replacements_dict = {
        'A': 't',
        'T': 'a',
        'C': 'g',
        'G': 'c'
    }

    for key, value in replacements_dict.items():
        if key in s:
            s = s.replace(key, value)

    return s.upper()
def reverse_complement(s):

    replacements_dict = {
        'A': 't',
        'T': 'a',
        'C': 'g',
        'G': 'c'
    }

    for key, value in replacements_dict.items():
        if key in s:
            s = s.replace(key, value)

    return s[::-1].upper()

def test_function(s):

    return s[0]
