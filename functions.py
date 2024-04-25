import json

import stmol
import py3Dmol
import requests
import biotite.structure.io as bsio

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
    """
    Transcribes the given DNA sequence into an RNA sequence.

    This function replaces all occurrences of 'T' in the DNA sequence with 'U' to obtain the RNA sequence.

    Parameters:
    - s (str): The DNA sequence to be transcribed.

    Returns:
    - str: The transcribed RNA sequence.
    """
    return s.replace('T', 'U')

def complement(s):
    """
    Finds the complementary sequence of a given DNA sequence.

    Parameters:
    - s (str): The DNA sequence for which the complementary sequence is to be found.

    Returns:
    - str: The complementary DNA sequence.
    """

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
    """
    Finds the reverse complement of a given DNA sequence.

    The function first finds the complement of the sequence and then reverses it.

    Parameters:
    - s (str): The DNA sequence for which the reverse complement is to be found.

    Returns:
    - str: The reverse complement of the DNA sequence.
    """

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


###
class DNAProcessor:

    START_CODON = "AUG"
    STOP_CODON_PROTEIN = "STOP"

    def __init__(self, sequence_input):
        """
        Initializes a new instance of the DNAProcessor class. Transcription is applied
        on the sequence_input to convert all T nucleotides to U nucleotides.

        Parameters:
        - sequence_input (string): The DNA sequence to process.
        """
        self.sequence = sequence_input.replace('T', 'U')
        self.codons = []
        self.proteins = []

    def find_start_codon(self):
        """
        Searches for the start codon "AUG" in the sequence and updates the sequence
        to begin from the end of the found start codon.

        Returns:
        - The updated DNAProcessor instance (self) for method chaining.
        """
        start_codon_index = self.sequence.find(DNAProcessor.START_CODON)
        if start_codon_index != -1:
            self.sequence = self.sequence[start_codon_index + 3:]
        return self

    def codons_structure(self):
        """
        Splits the sequence into codons (sets of 3 nucleotides) and stores them
        in the self.codons list.

        Returns:
        - The updated DNAProcessor instance (self) for method chaining.
        """
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]
            if len(codon) == 3:
                self.codons.append(codon)
            else:
                break
        return self

    def read_json_from_file(self, json_file):
        """
        Reads a JSON file and returns a dictionary containing codon-protein mappings.

        Parameters:
        - json_file (string): Path to the JSON file.

        Returns:
        - Dictionary containing codon-protein mappings.
        """
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data.get("codons", {})

    def find_proteins(self, codons_dict):
        """
        Maps codons to their respective proteins using the provided codons dictionary
        and stores the resulting proteins in the self.proteins list. The mapping stops
        if a STOP codon protein is encountered.

        Parameters:
        - codons_dict (dict): Dictionary containing codon-protein mappings.

        Returns:
        - The updated DNAProcessor instance (self) for method chaining.
        """
        for codon in self.codons:
            protein = codons_dict.get(codon.upper(), "Unknown")
            if protein == DNAProcessor.STOP_CODON_PROTEIN:
                break
            self.proteins.append(protein)
        return self

    def process(self, json_file):
        """
        Orchestrates the process of finding the start codon, determining codon structure,
        reading codon-protein mappings from a JSON file, and finding the corresponding proteins.

        Parameters:
        - json_file (string): Path to the JSON file containing codon-protein mappings.

        Returns:
        - List of proteins corresponding to the codons in the sequence.
        """
        codons_dict = self.read_json_from_file(json_file)
        self.find_start_codon().codons_structure().find_proteins(codons_dict)
        return self.proteins

# FOR LOCAL TESTING

# s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# dna_processor = DNAProcessor('AGAUGCUUUUCAUUCUGACUGCAACGGGCAAUAUGUCUCUGUGUGGAUUAAAAAAAGAGUGUCUGAUAGCAGC')
# dna_processor.find_start_codon()
# dna_processor.codons_structure()
# codons_dict = dna_processor.read_json_from_file('aminoacids_combination.json')
# dna_processor.find_proteins(codons_dict)


#
# # Assuming you have a JSON file named 'data.json'
# processor = DNAProcessor(s)
# resulting_proteins = processor.process('aminoacids_combination.json')


