from lexer import Lexer
from parser import Parser
from validator import Validator


def parse_json(json_str):
    lexer = Lexer(json_str)
    parser = Parser(lexer)
    parsed = parser.parse()
    Validator.validate(parsed)  # Optional now
    return parsed

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as f:
            json_str = f.read()
        result = parse_json(json_str)
        print("Valid JSON:", result)
    except ValueError as e:
        print("Invalid JSON:", e)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
