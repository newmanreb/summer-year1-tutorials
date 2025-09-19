# Import modules
from summer_year1_tutorials.utils.dna_integrity_check import dna_integrity_check
from summer_year1_tutorials.logger import logger

def translate_dna(sequence, start_position=1):
    """
    Translates a DNA sequence to protein.

    Parameters
    ----------
    sequence: str
        DNA sequence to be translated.
    start_position: int, optional
        Start position for translation. (1-based, default=1).

    Returns
    ----------
    protein_sequence: str
        Translated protein sequence in single-letter amino acid codes.

    Notes
    ----------
    Translation stops at the first stop codon (*) encountered. Uppercase enforced.
    """
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
    sequence = "".join(sequence.split()).upper()        # Remove whitespace and enforce uppercase input.
    logger.info(f"Translating {sequence} from position {start_position}.")
    dna_integrity_check(sequence)                       # Run integrity check to ensure all ATGC characters.
    logger.info(f"DNA sequence passes integrity check.")

    translate_this = sequence[start_position - 1:]      # Sets start position based on Python's 0-based indexing
    protein = ""                                        # Sets an empty protein string.
    for each_codon in range(0, len(translate_this)-2, 3):   # Loops over the input string 3 at a time, except final 2.
        codon = translate_this[each_codon:each_codon + 3]   # Defines one codon as each block of 3.

        if len(codon) == 3:
            amino_acid = codons.get(codon, "X")         # Finds the codon in the AA table matches the letter code.
            protein += amino_acid                       # Add the amino acid found to the protein string.
            if amino_acid == "*":                       # Stop codon handling.
                logger.info(f"Stop codon reached at codon {codon}.")
                break
        else:
            logger.warning(f"Incomplete codon {codon} skipped.")    # For instances where codon length is not 3.

    logger.info(f"Translated protein: {protein.upper()}")
    return protein.upper()

translation_sequence = "aggagtaagcccttgcaactggaaatacacccattg"
print(translate_dna(translation_sequence))

#challenge_sequence = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA"
#print(translate_dna(challenge_sequence))