import pytest
from summer_year1_tutorials.modules import chunk_text as ct

# ------------------------
# Standard chunking tests
# ------------------------
def test_chunk_text_dna_basic(monkeypatch):
    """Basic DNA sequence chunking with block_size=5"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = "AAAAABBBBBCCCCC"
    chunks = ct.chunk_text(sequence, 5, "DNA")
    assert chunks == ["AAAAA", "BBBBB", "CCCCC"]


def test_chunk_text_rna(monkeypatch, caplog):
    """RNA sequence chunking should skip DNA check and log chunked output"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = "GCUGAGACUUCCUGGACGGGGGACAGGCUGUGGGGUUUCUACG"

    with caplog.at_level("INFO"):
        chunks = ct.chunk_text(sequence, 10, "RNA")

    expected_chunks = [
        "GCUGAGACUU",
        "CCUGGACGGG",
        "GGACAGGCUG",
        "UGGGGUUUCU",
        "ACG"
    ]
    # Check returned chunks
    assert chunks == expected_chunks

    # Check logged output
    log_message = caplog.messages[-1]  # last INFO message is chunked sequence
    assert "\n".join(expected_chunks) in log_message


# ------------------------
# Edge case tests
# ------------------------
def test_chunk_text_empty_sequence(monkeypatch):
    """Empty sequence returns empty list"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    chunks = ct.chunk_text("", 5, "DNA")
    assert chunks == []


def test_chunk_text_block_size_larger_than_sequence(monkeypatch):
    """If block_size > sequence length, return single short chunk"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = "ATGC"
    chunks = ct.chunk_text(sequence, 10, "DNA")
    assert chunks == ["ATGC"]


def test_chunk_text_not_divisible(monkeypatch):
    """Sequence length not divisible by block_size produces shorter last chunk"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = "ATGCA"
    chunks = ct.chunk_text(sequence, 3, "DNA")
    assert chunks == ["ATG", "CA"]


def test_chunk_text_with_whitespace(monkeypatch):
    """Whitespace should be removed and letters uppercased"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = " atg c\n a t "
    chunks = ct.chunk_text(sequence, 2, "DNA")
    assert chunks == ["AT", "GC", "AT"]


# ------------------------
# Exception tests
# ------------------------
def test_chunk_text_non_string_sequence():
    """Non-string input sequence should raise AttributeError"""
    with pytest.raises(AttributeError):
        ct.chunk_text(12345, 2, "DNA")


def test_chunk_text_non_integer_block_size(monkeypatch):
    """Non-integer block_size should raise TypeError"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    with pytest.raises(TypeError):
        ct.chunk_text("ATGC", "not-an-int")


def test_chunk_text_non_alpha_warning(monkeypatch, caplog):
    """Sequence with non-alphabetic characters should log a warning"""
    monkeypatch.setattr(ct, "dna_integrity_check", lambda seq: True)
    sequence = "ATGC123"
    with caplog.at_level("WARNING"):
        ct.chunk_text(sequence, 3, "DNA")
    assert any("non-alphabetic characters" in message.lower() for message in caplog.messages)
