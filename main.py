import sys
import os

from compress import compress


def main(argv):
    operation, input_file, output_file = get_arguments(argv)

    file_name = ""
    if output_file:
        file_name = output_file
    else:
        file_name = input_file.replace('.txt', '.z78')

    if operation == '-c':
        compress(input_file, file_name)
    # elif operation == '-x':
    #     decompress


def get_arguments(argv):
    operation = ""
    input_file = ""
    output_file = ""

    if len(argv) >= 2:
        operation = argv[0]
        input_file = argv[1]
        if len(argv) == 4:
            output_file = argv[3]
    else:
        print('Invalid arguments')
        print(
            "main.py <OPERATION: -c COMPRESS || -x DECOMPRESS> <INPUT FILE> [-o OUTPUT FILE]"
        )
        os._exit(1)

    return operation, input_file, output_file


if __name__ == "__main__":
    main(sys.argv[1:])