import argparse


def count_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            byte_count = len(content)
            print(f"{byte_count} {file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"{line_count} {file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            word_count = sum(len(line.split()) for line in file)
            print(f"{word_count} {file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def count_chars(file_path):
    try:
        with open(file_path, 'r') as file:
            char_count = sum(1 + len(line) for line in file)
            print(f"{char_count} {file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Count bytes, lines, words, or characters in a file')
    parser.add_argument('-c', '--count', metavar='FILE', type=str,
                        help='File for which to count bytes')
    parser.add_argument('-l', '--lines', metavar='FILE', type=str,
                        help="File for which to count lines")
    parser.add_argument('-w', '--words', metavar='FILE', type=str,
                        help='File for which to count words')
    parser.add_argument('-m', '--chars', metavar='FILE', type=str,
                        help='File for which to count characters')

    args = parser.parse_args()

    if args.count:
        count_bytes(args.count)
    elif args.lines:
        count_lines(args.lines)
    elif args.words:
        count_words(args.words)
    elif args.chars:
        count_chars(args.chars)
    else:
        print("Error: Please provide a file path following either '-c' '-l' '-w' or '-m' option.")

if __name__ == "__main__":
    main()
