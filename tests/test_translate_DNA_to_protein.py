import pytest
from unittest.mock import patch
import summer_year1_tutorials.modules.translate_DNA_to_protein as tr

# ------------------------
# Basic translation tests
# ------------------------
def test_translate_basic(monkeypatch):
    """Translate a simple DNA sequence to protein"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    seq = "ATGGTTTAA"
    result = tr.translate_dna(seq)
    assert result == "MV*"  # ATG=M, GTT=V, TAA=Stop

def test_translate_partial_codon(monkeypatch):
    """Handles sequence where last codon is incomplete"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    seq = "ATGG"  # Last codon "G" is incomplete
    result = tr.translate_dna(seq)
    assert result == "M"  # Only full codons are translated

def test_translate_with_start_position(monkeypatch):
    """Translation starting from a non-default position"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    seq = "ATGTTTAA"
    result = tr.translate_dna(seq, start_position=4)
    assert result == "F"  # Start at position 4 → codons: TTT=T, AA incomplete

# ------------------------
# Stop codon tests
# ------------------------
def test_translate_stops_at_first_stop(monkeypatch):
    """Translation should stop at first stop codon"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    seq = "ATGTAACTG"  # TAA is stop codon
    result = tr.translate_dna(seq)
    assert result == "M*"  # Stops at first stop

# ------------------------
# Logging tests
# ------------------------
def test_translate_logging(monkeypatch, caplog):
    """Logger.info should record translation steps and stop codon"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    seq = "ATGTAA"
    with caplog.at_level("INFO"):
        result = tr.translate_dna(seq)
    assert "stop codon reached" in " ".join(caplog.messages).lower()
    assert "translated protein: m*" in " ".join(caplog.messages).lower()

# ------------------------
# Edge case tests
# ------------------------
def test_translate_empty_sequence(monkeypatch):
    """Empty sequence returns empty protein"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    result = tr.translate_dna("")
    assert result == ""

# ------------------------
# Exception tests
# ------------------------
def test_translate_non_string_input():
    """Non-string input raises TypeError"""
    with pytest.raises(TypeError):
        tr.translate_dna(1234)