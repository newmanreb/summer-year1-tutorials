import pytest
import summer_year1_tutorials.modules.transcribe_DNA_to_RNA as tr
from unittest.mock import MagicMock
from unittest.mock import patch

# ------------------------
# Basic transcription
# ------------------------
def test_transcribe_basic(monkeypatch):
    """Transcribes standard DNA to RNA, lowercase, full sequence"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    dna = "ATGC"
    rna = tr.transcribe(dna)
    assert rna == "augc"

def test_transcribe_start_position(monkeypatch):
    """Transcription starts at start_position (1-based)"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    dna = "GATTACA"
    rna = tr.transcribe(dna, start_position=3)  # should start at "TTACA"
    assert rna == "uuaca"  # 'T' -> 'U', lowercase

def test_transcribe_whitespace(monkeypatch):
    """DNA with whitespace is cleaned before transcription"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    dna = " G A T T A C A \n"
    rna = tr.transcribe(dna)
    assert rna == "gauuaca"

def test_transcribe_thymine_to_uracil(monkeypatch):
    """All T's are converted to U's in RNA"""
    monkeypatch.setattr(tr, "dna_integrity_check", lambda seq: True)
    dna = "TTTT"
    rna = tr.transcribe(dna)
    assert rna == "uuuu"

# ------------------------
# Exception / edge cases
# ------------------------
def test_transcribe_non_string():
    """Non-string input should raise AttributeError"""
    with pytest.raises(AttributeError):
        tr.transcribe(12345)

def test_transcribe_invalid_dna(monkeypatch):
    """Invalid DNA sequence raises ValueError via dna_integrity_check"""
    def fake_check(seq):
        raise ValueError("Invalid DNA")
    monkeypatch.setattr(tr, "dna_integrity_check", fake_check)
    with pytest.raises(ValueError):
        tr.transcribe("ATGX")

# ------------------------
# Logging tests
# ------------------------
def test_transcribe_logging():
    """Logger.info should record the cleaned DNA and transcribed RNA"""
    with patch.object(tr, "dna_integrity_check", return_value=True):
        with patch.object(tr.logger, "info") as mock_log:
            rna = tr.transcribe("GATTACA")

    # The logger should be called at least once with the transcribed RNA
    assert any("gauuaca" in str(call.args[0]) for call in mock_log.call_args_list)
    # The logger should also mention the cleaned DNA
    assert any("GATTACA" in str(call.args[0]) for call in mock_log.call_args_list)