import re

class TokenType:
    LBRACE = '{'
    RBRACE = '}'
    LBRACKET = '['
    RBRACKET = ']'
    COLON = ':'
    COMMA = ','
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    NULL = 'NULL'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class Lexer:
    def __init__(self, input_str):
        self.input = input_str
        self.pos = 0

    def next_token(self):
        while self.pos < len(self.input) and self.input[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.input):
            return None

        current_char = self.input[self.pos]

        if current_char in '{}[]:,':
            self.pos += 1
            return Token(current_char, current_char)

        if current_char == '"':
            return self._read_string()

        if current_char.isdigit() or current_char == '-':
            return self._read_number()

        if self.input.startswith('true', self.pos):
            self.pos += 4
            return Token(TokenType.TRUE, True)
        if self.input.startswith('false', self.pos):
            self.pos += 5
            return Token(TokenType.FALSE, False)
        if self.input.startswith('null', self.pos):
            self.pos += 4
            return Token(TokenType.NULL, None)

        raise ValueError(f"Unexpected character: {current_char}")

    def _read_string(self):
        self.pos += 1
        start = self.pos
        while self.pos < len(self.input) and self.input[self.pos] != '"':
            if self.input[self.pos] == '\\':
                self.pos += 1
            self.pos += 1
        if self.pos >= len(self.input):
            raise ValueError("Unterminated string")
        val = self.input[start:self.pos]
        self.pos += 1
        return Token(TokenType.STRING, val)

    def _read_number(self):
        num_regex = re.compile(r'-?\d+(\.\d+)?([eE][+-]?\d+)?')
        match = num_regex.match(self.input, self.pos)
        if not match:
            raise ValueError("Invalid number format")
        self.pos = match.end()
        value = match.group()
        return Token(TokenType.NUMBER, float(value) if '.' in value or 'e' in value or 'E' in value else int(value))
