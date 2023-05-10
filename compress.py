from functools import reduce
from math import ceil
from trie import Trie

BIG = 'big'
CHAR_SIZE = 1


def reduce_function(accumulators: tuple[Trie, bytes, str], char):
    dictionary = accumulators[0]
    output = accumulators[1]
    string = accumulators[2]

    if dictionary.find(string + char) > -1:
        string = string + char

    else:
        code = dictionary.find(string)
        code_size = ceil(code.bit_length() / 8.0)
        num_char = ord(char)

        output += code_size.to_bytes(1, BIG) + code.to_bytes(
            code_size, BIG) + num_char.to_bytes(CHAR_SIZE, BIG)

        dictionary.insert(string + char)
        string = ''

    return (dictionary, output, string)


def compress(input_file, output_file):
    input = ""
    with open(input_file, 'r', encoding="utf-8") as file:
        input = file.read()

    dictionary, output, string = reduce(reduce_function, input,
                                        (Trie(), bytes(), ''))

    code = dictionary.find(string)
    code_size = ceil(code.bit_length() / 8.0)
    output += code_size.to_bytes(1, BIG) + code.to_bytes(code_size, BIG)

    with open(output_file, 'wb') as file:
        file.write(output)