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


def main():
    parser = argparse.ArgumentParser(description='wc tool for word line character and byte count.')
    parser.add_argument('-c', '--count', metavar='FILE', type=str,
                        help='The file path requested to run byte count command')
    parser.add_argument('-l', '--lines', metavar='FILE', type=str,
                        help="File for which to count lines")

    args = parser.parse_args()

    if args.count:
        count_bytes(args.count)
    elif args.lines:
        count_lines(args.lines)
    else:
        print("Error: Please provide a file path with either '-c' or '-l' option.")

if __name__ == "__main__":
    main()
