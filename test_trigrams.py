import pytest


def test_read_file():
    from trigrams import read_file
    assert  len(read_file(INPUT_FILE)) > 500 