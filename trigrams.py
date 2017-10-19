my_string = """It was the best of times. It was the worst of times."""

the_sequence = {}


def read_file(text_file, result_file=None):
    """This function will open the text file to be read."""
    the_file = open(text_file, 'r')
    data = the_file.read()
    the_file.close()
    return data


def create_dict(file_name):
    new_string = file_name.split()
    for index, item in enumerate(new_string):
        if index < len(new_string) - 2:
            dic_key = new_string[index] + " " + new_string[index + 1]
            if dic_key in the_sequence:
                the_sequence[dic_key].append(new_string[index + 2])
                print("This is a duplicate item")
            else:
                the_sequence[dic_key] = [new_string[index + 2]]
    for item in the_sequence:
        print(item + " ---- " + str(the_sequence[item]))

#create_dict(my_string)
create_dict(read_file('test_text.txt'))
