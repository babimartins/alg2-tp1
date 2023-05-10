from functools import reduce
from math import ceil
from trie import Trie

BIG = "big"
CHAR_SIZE = 1


def compress(input_file, output_file):
    input = ""
    with open(input_file, "r", encoding="utf-8") as file:
        input = file.read()

    init = [Trie(), bytes(), ""]
    dictionary, output, string = reduce(__reduce_function, input, init)

    index = dictionary.find(string)
    index_size = ceil(index.bit_length() / 8.0)
    output += index_size.to_bytes(1, BIG) + index.to_bytes(index_size, BIG)

    with open(output_file, "wb") as file:
        file.write(output)


def __reduce_function(tuples: tuple[Trie, bytes, str], char):
    dictionary = tuples[0]
    output = tuples[1]
    string = tuples[2]

    if dictionary.find(string + char) > -1:
        string = string + char

    else:
        index = dictionary.find(string)
        index_size = ceil(index.bit_length() / 8.0)
        num_char = ord(char)

        output += index_size.to_bytes(1, BIG) + index.to_bytes(
            index_size, BIG) + num_char.to_bytes(CHAR_SIZE, BIG)

        dictionary.insert(string + char)
        string = ""

    return (dictionary, output, string)