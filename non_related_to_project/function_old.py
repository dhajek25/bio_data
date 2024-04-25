import json
s_u = 'AGAUGCUUUUCAUUCUGACUGCAACGGGCAAUAUGUCUCUGUGUGGAUUAAAAAAAGAGUGUCUGAUAGCAGC'

def find_start_codon(mrna_sequence):

    start_codon = "AUG"

    start_codon_index = mrna_sequence.find(start_codon)

    if start_codon_index != -1:
        mrna_without_start_codon = mrna_sequence[start_codon_index + 3:]

    return mrna_without_start_codon


def codons_structure(mrna_without_start_codon):

    codons = []

    for i in range(0, len(mrna_without_start_codon), 3):
        codon = mrna_without_start_codon[i:i+3]

        if len(codon) == 3:
            codons.append(codon)
        else:
            break

    return codons

def read_codons_from_json(json_file):
    # Read the JSON file and load it as a dictionary
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract the codons and proteins from the JSON data
    codons_dict = data.get("codons", {})

    return codons_dict

def find_proteins(codons_list, codons_dict):
    proteins = []
    for codon in codons_list:
        protein = codons_dict.get(codon.upper(), "Unknown")

        if protein != 'STOP':
            proteins.append(protein)
        else:
            break
    return proteins
