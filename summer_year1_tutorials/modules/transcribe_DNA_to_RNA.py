## Import modules
from summer_year1_tutorials.utils.dna_integrity_check import dna_integrity_check
from summer_year1_tutorials.logger import logger

def transcribe(dna_seq, start_position=1):
    """
    Transcribes a DNA sequence to RNA.

    Parameters
    ----------
    dna_seq : str
        DNA sequence to transcribe.
    start_position: int, optional
        Start position for transcription. (1-based, default=1).

    Returns
    ----------
    str
        Transcribed RNA sequence.

    Notes
    ----------
    Converts thymine (T) to uracil (U) and enforces lowercase RNA alphabet.
    """
    dna_seq = "".join(dna_seq.split()).upper()          # Remove whitespace and force uppercase on input.
    logger.info(f"Transcribing DNA to RNA from position {start_position}: {dna_seq}")
    dna_integrity_check(dna_seq)                        # Run integrity check to ensure all ATGC characters.
    logger.info(f"DNA sequence passes integrity check.")

    transcribe_this = dna_seq[start_position - 1:]      # Sets start position based on Python's 0-based indexing
    rna_seq = transcribe_this.replace("T", "U").lower() # Transcribes the DNA and forces lowercase.
    logger.info(f"Transcribed RNA: {rna_seq}")

    return rna_seq

if __name__ == "__main__":  # pragma: no cover
    example_seq = "aggagtaagcccttgcaactggaaatacacccattg"
    transcribe(example_seq)