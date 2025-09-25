import pytest
from unittest.mock import patch
import summer_year1_tutorials.modules.genbank_style as gb

# ------------------------
# Basic formatting tests
# ------------------------
def test_genbank_basic(monkeypatch):
    """Basic formatting with default block_size=10 and blocks_per_row=6"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    seq = "ATGCATGCATGCATGCATGCATGCATGCATGCATGC"  # 39 chars
    result = gb.genbank_format(seq)

    # Build expected first row dynamically
    blocks = ["atgcatgcat", "gcatgcatgc", "atgcatgcat", "gcatgc"]
    expected_start = "1        " + " ".join(blocks)
    assert result.startswith(expected_start)

    # Output should be lowercase
    assert result.islower()

def test_genbank_custom_block_row(monkeypatch):
    """Custom block size and blocks per row"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    seq = "ATGCATGCATGCATGC"
    # block_size=4, blocks_per_row=2 → row_size=8
    result = gb.genbank_format(seq, block_size=4, blocks_per_row=2)
    expected = "1        atgc atgc\n9        atgc atgc"
    assert result == expected

def test_genbank_whitespace(monkeypatch):
    """Input with spaces and newlines should be cleaned"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    seq = "AT GC\nATGC"
    result = gb.genbank_format(seq, block_size=2, blocks_per_row=2)

    # Expect two rows
    expected = "1        at gc\n5        at gc"
    assert result == expected

# ------------------------
# Logging tests
# ------------------------
def test_genbank_non_alpha_warning(monkeypatch, caplog):
    """Non-alphabetic characters trigger warning"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    seq = "ATGC123"
    with caplog.at_level("WARNING"):
        gb.genbank_format(seq)
    assert any("non-alphabetic characters" in msg.lower() for msg in caplog.messages)

def test_genbank_seq_type_logging(monkeypatch, caplog):
    """Custom seq_type logs type info if not DNA"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    with caplog.at_level("INFO"):
        gb.genbank_format("ATGC", seq_type="RNA")
    assert any("sequence type provided: rna" in msg.lower() for msg in caplog.messages)

# ------------------------
# Edge case tests
# ------------------------
def test_genbank_empty_sequence(monkeypatch):
    """Empty input should return empty string"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    result = gb.genbank_format("")
    assert result == ""

def test_genbank_short_sequence(monkeypatch):
    """Sequence shorter than a row still formats correctly"""
    monkeypatch.setattr(gb, "dna_integrity_check", lambda seq: True)
    seq = "ATGCAT"
    result = gb.genbank_format(seq, block_size=2, blocks_per_row=3)
    expected = "1        at gc at"
    assert result == expected

# ------------------------
# Exception tests
# ------------------------
def test_genbank_non_string_input():
    """Non-string input should raise TypeError"""
