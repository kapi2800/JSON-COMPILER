import unittest
from src.parser import Parser
from src.lexer import Lexer

class TestParser(unittest.TestCase):
    def test_parse_object(self):
        json_str = '{"name": "Alice"}'
        lexer = Lexer(json_str)
        parser = Parser(lexer)
        result = parser.parse()
        self.assertEqual(result, {"name": "Alice"})

if __name__ == "__main__":
    unittest.main()
