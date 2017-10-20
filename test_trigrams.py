import pytest


def test_read_file():
    """This function tests that input file has more than 500 chars."""
    from trigrams import read_file
    assert len(read_file('input_text.txt')) > 500


def test_new_string():
    """This function tests that new_string splits input text."""
    from trigrams import create_dict
    create_dict(read_file('input_text.txt'))
    assert len(the_sequence) > 1


def test_dic_key():
    """This function tests that keys are being made in pairs."""
    from trigrams import create_dict
    assert len(create_dict('test_text.txt')) == 2
    #assert len(dic_key) == 2

def test_the_sequence():
    """This function will test that key value pairs are being appended to the dictionary"""
    from trigrams import the_sequence
    assert len(the_sequence) > 0


def test_write_madness():
    """This will test that a new paragraph is being written."""
    from trigrams import write_madness
    assert len(write_madness('so', 'she')) > 2


def test_write_file():
    """This will test that a output file is being written."""
    from trigrams import write_file
    assert len(output_file) > 2
