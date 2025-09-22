import string
from summer_year1_tutorials.logger import logger

def dna_integrity_check(seq):
    """
    This utility checks that DNA sequences are strings and contain only ATGC characters, providing a warning
    if uracil (U) is found, suggesting an RNA sequence was provided instead.

    Parameters
    ----------
    seq: str
        Input sequence for integrity check.

    Returns
    ----------
    str
        Confirmation message: "Input sequence is DNA." if the sequence passes all integrity checks.

    Raises
    ----------
    TypeError
        If the input is not a string.
    ValueError
        If the input contains invalid bases (anything other than ATGC characters).
        If the sequence contains Uracil (U), suggesting an RNA sequence.
    """
    # Check that input is a string
    if not isinstance(seq, str):
        logger.error("Sequence input must be a string.")
        raise TypeError("Sequence input must be a string.")

    # Check for Uracil in input
    if "u" in seq.lower():
        logger.error("Uracil (U) found in sequence, check that sequence is DNA not RNA.")
        raise ValueError("Uracil (U) found in sequence, input appears to be RNA not DNA.")

    # Check for invalid bases
    seq_chars = set(seq.lower()).difference(
        set(string.whitespace))     # Extract unique characters from seq, excluding whitespace)
    if not seq_chars.issubset("atcg"):
        logger.error("Invalid base found in sequence, only use ATGC characters.")
        raise ValueError("Invalid base found in sequence, only use ATGC characters.")

    return "Input sequence is DNA."
