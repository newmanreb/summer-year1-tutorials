# genbank_style.py
# Import modules
from summer_year1_tutorials.utils.dna_integrity_check import dna_integrity_check
from summer_year1_tutorials.logger import logger

def genbank_format(sequence, block_size=10, blocks_per_row=6, seq_type="DNA"):
    """
    Displays an input string in GenBank format, with 10 characters per block and 6 blocks per row (default).

    Parameters
    ----------
    sequence: str
        Sequence to be formatted.
    block_size: int
        The length of each block. Defaults to 10.
    blocks_per_row: int
        The number of blocks per row. Defaults to 6.
    seq_type:
        Input type. If "DNA", an integrity check is performed on the input sequence.

    Returns
    ----------
    str
        Input sequence separated by blocks and rows. Lowercase enforced.

    Raises
    ----------
    TypeError
        If the input type is not a string or if block_size and blocks_per_row are not integers.
    ValueError
        If seq_type is "DNA" and the sequence contains uracil (U).
        If seq_type is "DNA" and the sequence contains invalid bases (anything other than A, T, G, or C).
    """
    sequence = "".join(sequence.split()).lower()        # Remove whitespace and force lowercase on input.

    if not sequence.isalpha():                          # Check for non-alpha characters in input.
        logger.warning("Sequence contains non-alphabetic characters. Check input for digits or symbols.")

    if seq_type == "DNA":                               # If input type is DNA, run integrity check.
        dna_integrity_check(sequence)                   # Ensure all ATGC characters in DNA sequence.
        logger.info(f"Input DNA sequence passes integrity check.")
    else:                                               # Print user-provided sequence type to the log.
        logger.info(f"Sequence type provided: {seq_type}")

    logger.info("Chunking sequence '{}' into blocks of {}, with {} blocks per row".format(sequence, block_size,
                                                                                          blocks_per_row))

    row_size = block_size * blocks_per_row

    try:
        for start in range(0, len(sequence), row_size):
            row_seq = sequence[start:start + row_size]

            blocks = []
            for i in range(0, len(row_seq), block_size):
                block = row_seq[i:i + block_size]
                blocks.append(block)

            formatted_row = ' '.join(blocks)
            print(f"{start + 1:<9}{formatted_row}")
    except TypeError as e:
        logger.error("Chunking failed with exception: {}".format(e))
        raise

sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"
sequence2 = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTC"
genbank_format(sequence2)
