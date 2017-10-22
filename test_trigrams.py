"""For testing trigrams.py."""
import pytest


def test_read_file():
    """The function tests that input file has more than 500 chars."""
    from trigrams import read_file
    assert len(read_file('input_text.txt')) > 500


def test_new_string():
    """The function tests that new_string splits input text."""
    from trigrams import read_file, create_dict, the_sequence
    create_dict(read_file('input_text.txt'))
    assert len(the_sequence) > 1


def test_dic_key():
    """The function tests that keys are being made in pairs."""
    from trigrams import read_file, create_dict, the_sequence
    x = read_file('test_text.txt')
    create_dict(x)
    assert len(the_sequence) > 0


def test_the_sequence():
    """Will test kv pairs are being appended to the dictionary."""
    from trigrams import the_sequence
    assert len(the_sequence) > 0


def test_write_madness():
    """Will test that a new paragraph is being written."""
    from trigrams import write_madness
    assert len(write_madness('so', 'she')) > 2
