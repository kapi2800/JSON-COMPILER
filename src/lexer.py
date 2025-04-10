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

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Lexer:
    def __init__(self, input_str):
        self.input = input_str
        self.pos = 0
    
    def next_token(self):
        if self.pos >= len(self.input):
            return None
        
        # Skip whitespace
        while self.pos < len(self.input) and self.input[self.pos].isspace():
            self.pos += 1
        
        # Handle single-character tokens
        current_char = self.input[self.pos]
        if current_char in ['{', '}', '[', ']', ':', ',']:
            self.pos += 1
            return Token(current_char, current_char)
        
        # Handle strings
        if current_char == '"':
            return self._read_string()
        
        # Handle numbers
        if current_char.isdigit() or current_char == '-':
            return self._read_number()
        
        # Handle true/false/null
        if self.input.startswith('true', self.pos):
            self.pos += 4
            return Token(TokenType.TRUE, 'true')
        elif self.input.startswith('false', self.pos):
            self.pos += 5
            return Token(TokenType.FALSE, 'false')
        elif self.input.startswith('null', self.pos):
            self.pos += 4
            return Token(TokenType.NULL, 'null')
        
        raise ValueError(f"Unexpected character: {current_char}")
    
    def _read_string(self):
        self.pos += 1  # Skip opening quote
        start_pos = self.pos
        while self.pos < len(self.input) and self.input[self.pos] != '"':
            if self.input[self.pos] == '\\':  # Handle escape sequences
                self.pos += 1
            self.pos += 1
        if self.pos >= len(self.input):
            raise ValueError("Unterminated string")
        string_val = self.input[start_pos:self.pos]
        self.pos += 1  # Skip closing quote
        return Token(TokenType.STRING, string_val)
    
    def _read_number(self):
        num_regex = re.compile(r'-?\d+(\.\d+)?([eE][+-]?\d+)?')
        match = num_regex.match(self.input, self.pos)
        if not match:
            raise ValueError("Invalid number format")
        self.pos = match.end()
        return Token(TokenType.NUMBER, float(match.group()) if '.' in match.group() else int(match.group()))
    
