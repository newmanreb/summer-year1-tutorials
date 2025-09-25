# chunk_text.py
# Import modules
from summer_year1_tutorials.utils.dna_integrity_check import dna_integrity_check
from summer_year1_tutorials.logger import logger

def chunk_text(sequence, block_size, seq_type="DNA"):
    """
    Splits a DNA sequence into evenly sized blocks and formats them into a list of chunked sequences.

    Parameters
    ----------
    sequence: str
        Sequence to chunk.
    block_size: int
        The length of each block/chunk.
    seq_type: str
        Input type. If "DNA", an integrity check is performed on the input sequence.

    Returns
    ----------
    str
        Chunked sequence by block_size.

    Raises
    ----------
    TypeError
        If block_size is not an integer.
    AttributeError
        If the input type is not a string.
    ValueError
        If seq_type is "DNA" and the sequence contains uracil (U).
        If seq_type is "DNA" and the sequence contains invalid bases (anything other than A, T, G, or C).
    """
    sequence = "".join(sequence.split()).upper()        # Remove whitespace and force uppercase on input.

    if not sequence.isalpha():                          # Check for non-alpha characters in input.
        logger.warning("Sequence contains non-alphabetic characters. Check input for digits or symbols.")

    if seq_type == "DNA":                               # If input type is DNA, run integrity check.
        dna_integrity_check(sequence)                   # Ensure all ATGC characters in DNA sequence.
        logger.info(f"Input DNA sequence passes integrity check.")
    else:                                               # Print user-provided sequence type to the log.
        logger.info(f"Sequence type provided: {seq_type}")

    logger.info("Chunking sequence '{}' into blocks of {}".format(sequence, block_size))

    chunks = []                                         # Create an empty list to store each chunk
    index = 0                                           # Start index at the beginning of the sequence

    try:
        while index < len(sequence):                    # Continue looping until end of sequence
            block = sequence[index: index + block_size] # Extract slice of seq from 'index' to 'index + block_size'
            chunks.append(block)                        # Add this chunk to the list
            index += block_size                         # Increase the index by the block size to keep going
    except TypeError as e:
        logger.error("Chunking failed with exception: {}".format(e))
        raise

    chunked_str = "\n".join(chunks)
    logger.info(f"Chunked sequence:\n{chunked_str}")

    return chunks

if __name__ == "__main__":  # pragma: no cover
    sequence2 = "GCUGAGACUUCCUGGACGGGGGACAGGCUGUGGGGUUUCUACG"
    chunk_text(sequence2, 10, "RNA")