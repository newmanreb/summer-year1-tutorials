# tests/test_dna_integrity_check.py
import pytest
from summer_year1_tutorials.utils import dna_integrity_check as dic

def test_valid_dna_sequence():
    """Valid DNA sequence returns confirmation string."""
    seq = "ATGCATGC"
    result = dic.dna_integrity_check(seq)
    assert result == "Input sequence is DNA."

def test_non_string_input():
    """Non-string input raises TypeError."""
    with pytest.raises(TypeError):
        dic.dna_integrity_check(1234)

def test_sequence_with_uracil():
    """Sequence containing U raises ValueError."""
    seq = "AUGC"
    with pytest.raises(ValueError):
        dic.dna_integrity_check(seq)

def test_sequence_with_invalid_base():
    """Sequence containing invalid bases raises ValueError."""
    seq = "ATGBX"
    with pytest.raises(ValueError):
        dic.dna_integrity_check(seq)

def test_sequence_with_whitespace():
    """Whitespace in valid sequence is ignored."""
    seq = " A T G C "
    result = dic.dna_integrity_check(seq)
    assert result == "Input sequence is DNA."