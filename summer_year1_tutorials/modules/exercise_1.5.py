## 1.5
# Write code to transcribe a DNA sequence to RNA.
# Given the following sequence:
example_seq = "aggagtaagcccttgcaactggaaatacacccattg"
# The output should be "aggaguaagcccuugcaacuggaaauacacccauug"

from summer_year1_tutorials import logger
from summer_year1_tutorials


def transcribe(dna_seq):
    """Transcribes DNA to RNA by replacing T with U."""
    return dna_seq.upper().replace("T","U")

rna_seq_example = transcribe(example_seq)
print("RNA Example Sequence:", rna_seq_example.lower())

# Now given the following sequence, transcribe to RNA:
DNA = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"

RNA = transcribe(DNA)
print("RNA Sequence:", RNA)