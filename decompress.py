BIG = 'big'
CHAR_SIZE = 1


def decompress(input_file, output_file):

    output = ""
    with open(input_file, 'rb') as file:
        values = ['']
        index_size = int.from_bytes(file.read(CHAR_SIZE), BIG)
        index = int.from_bytes(file.read(index_size), BIG)
        char = file.read(CHAR_SIZE)
        string: str = ''
        while char:
            char = chr(ord(char))
            string = values[index] + char

            output += string
            values.append(string)

            index_size = int.from_bytes(file.read(1), BIG)
            index = int.from_bytes(file.read(index_size), BIG)
            char = file.read(CHAR_SIZE)

    string = values[index]
    output += string

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(output)