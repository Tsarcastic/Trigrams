import pytest


def test_read_file():
    from trigrams import read_file
    assert len(read_file('test_text.txt')) > 100