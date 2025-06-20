import sys
from lexer import Lexer
from parser import Parser
from validator import Validator

def parse_json(json_str):
    lexer = Lexer(json_str)
    parser = Parser(lexer)
    parsed = parser.parse()
    Validator.validate(parsed)
    return parsed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path-to-json-file>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as f:
            json_str = f.read()
        result = parse_json(json_str)
        print("Valid JSON:", result)
    except ValueError as e:
        print("Invalid JSON:", e)
    except FileNotFoundError:
        print("File not found:", sys.argv[1])
