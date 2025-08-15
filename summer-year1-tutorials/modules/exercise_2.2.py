# 2.2: Write a function to translate a DNA sequence into an amino acid sequence (without importing modules).
# Find the standard genetic code table online, and create a dictionary to hold a translational table.
# Use single letter amino-acid codes, and assume coding starts from the first base only.

translation_sequence = "aggagtaagcccttgcaactggaaatacacccattg"

def translate_dna(sequence):
    codons = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "ATT": "I",
        "ATC": "I", "ATA": "I", "ATG": "M", "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "TCT": "S", "TCC": "S",
        "TCA": "S", "TCG": "S", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACT": "T", "ACC": "T", "ACA": "T",
        "ACG": "T", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A", "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAT": "D",
        "GAC": "D", "GAA": "E", "GAG": "E", "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W", "CGT": "R", "CGC": "R",
        "CGA": "R", "CGG": "R", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGT": "G", "GGC": "G", "GGA": "G",
        "GGG": "G",
    }
    sequence = sequence.upper()
    protein = ""
    for each_codon in range(0, len(sequence)-2, 3):
        codon = sequence[each_codon:each_codon+3]
        amino_acid = codons.get(codon, "X")
        protein += amino_acid

    return protein

print(translate_dna(translation_sequence))

challenge_sequence = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA"
print(translate_dna(challenge_sequence))