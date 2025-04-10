from lexer import TokenType, Token

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
    
    def parse(self):
        if self.current_token.type == TokenType.LBRACE:
            return self._parse_object()
        elif self.current_token.type == TokenType.LBRACKET:
            return self._parse_array()
        else:
            return self._parse_value()
    
    def _parse_object(self):
        obj = {}
        self._consume(TokenType.LBRACE)
    
        if self.current_token.type == TokenType.RBRACE:
            self._consume(TokenType.RBRACE)
            return obj

        while True:
            key = self._parse_string()
            self._consume(TokenType.COLON)
            value = self.parse()
            obj[key] = value

            if self.current_token.type == TokenType.COMMA:
                self._consume(TokenType.COMMA)
            elif self.current_token.type == TokenType.RBRACE:
                self._consume(TokenType.RBRACE)
                break
            else:
                raise ValueError(f"Expected ',' or '}}', got {self.current_token.type}")

        return obj

    
    def _parse_string(self):
        if self.current_token.type != TokenType.STRING:
            raise ValueError(f"Expected STRING, got {self.current_token.type}")
        value = self.current_token.value
        self._consume(TokenType.STRING)
        return value

    
    def _parse_array(self):
        arr = []
        self._consume(TokenType.LBRACKET)
        while self.current_token.type != TokenType.RBRACKET:
            arr.append(self.parse())
            if self.current_token.type == TokenType.COMMA:
                self._consume(TokenType.COMMA)
            else:
                break
        self._consume(TokenType.RBRACKET)
        return arr
    
    def _parse_value(self):
        token = self.current_token
        if token.type == TokenType.STRING:
            self._consume(TokenType.STRING)
            return token.value
        elif token.type == TokenType.NUMBER:
            self._consume(TokenType.NUMBER)
            return token.value
        elif token.type == TokenType.TRUE:
            self._consume(TokenType.TRUE)
            return True
        elif token.type == TokenType.FALSE:
            self._consume(TokenType.FALSE)
            return False
        elif token.type == TokenType.NULL:
            self._consume(TokenType.NULL)
            return None
        else:
            raise ValueError(f"Unexpected token: {token.type}")
    
    def _consume(self, expected_type):
        if self.current_token.type == expected_type:
            self.current_token = self.lexer.next_token()
        else:
            raise ValueError(f"Expected {expected_type}, got {self.current_token.type}")