"""This module reads a file then uses predictive text to write a sample."""
import random
import sys
my_string = """It was the best of times. It was the blerst of times."""
the_sequence = {}
INPUT_FILE = 'input_text.txt'


def read_file(text_file):
    """The function will open the text file to be read."""
    the_file = open(text_file, 'r', encoding="utf8")
    data = the_file.read()
    the_file.close()
    return data


def create_dict(file_name):
    """The function creates a dictionary from the submitted file."""
    new_string = file_name.split()
    for index, item in enumerate(new_string):
        if index < len(new_string) - 2:
            dic_key = new_string[index] + " " + new_string[index + 1]
            if dic_key in the_sequence:
                the_sequence[dic_key].append(new_string[index + 2])
            else:
                the_sequence[dic_key] = [new_string[index + 2]]


def write_madness(word1, word2, num_words=50):
    """The function creates a story from the dict at inputed length."""
    paragraph = [word1, word2]
    for x in range(num_words):
        new = paragraph[-2] + " " + paragraph[-1]
        to_be_added = random.choice(the_sequence[new])
        paragraph.append(to_be_added)
    paragraph = " ".join(paragraph)
    return paragraph


def write_file(output_file, new_story):
    """The function will write a new file with the created story."""
    new_file = open(output_file, 'w')
    new_file.write(new_story)
    new_file.close()


def main(file, words):  # pragma: no cover
    """The whole enchilada from start to finish."""
    create_dict(read_file(file))
    x = write_madness("so", "she", int(words))
    write_file('stdout.txt', x)

create_dict(read_file('test_text.txt'))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
