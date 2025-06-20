from lexer import TokenType, Token

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def parse(self):
        value = self._parse_value()
        if self.current_token is not None:
            raise ValueError("Extra data after root JSON value")
        return value

    def _parse_object(self):
        obj = {}
        self._consume(TokenType.LBRACE)
        if self.current_token.type == TokenType.RBRACE:
            self._consume(TokenType.RBRACE)
            return obj

        while True:
            if self.current_token.type != TokenType.STRING:
                raise ValueError(f"Expected STRING as key, got {self.current_token.type}")
            key = self.current_token.value
            self._consume(TokenType.STRING)
            self._consume(TokenType.COLON)
            value = self._parse_value()
            obj[key] = value
            if self.current_token.type == TokenType.COMMA:
                self._consume(TokenType.COMMA)
            else:
                break

        self._consume(TokenType.RBRACE)
        return obj

    def _parse_array(self):
        arr = []
        self._consume(TokenType.LBRACKET)
        if self.current_token.type == TokenType.RBRACKET:
            self._consume(TokenType.RBRACKET)
            return arr

        while True:
            arr.append(self._parse_value())
            if self.current_token.type == TokenType.COMMA:
                self._consume(TokenType.COMMA)
            else:
                break

        self._consume(TokenType.RBRACKET)
        return arr

    def _parse_value(self):
        token = self.current_token
        if token.type == TokenType.LBRACE:
            return self._parse_object()
        elif token.type == TokenType.LBRACKET:
            return self._parse_array()
        elif token.type in [TokenType.STRING, TokenType.NUMBER, TokenType.TRUE, TokenType.FALSE, TokenType.NULL]:
            self._consume(token.type)
            return token.value
        else:
            raise ValueError(f"Unexpected token: {token.type}")

    def _consume(self, expected_type):
        if self.current_token is None or self.current_token.type != expected_type:
            raise ValueError(f"Expected {expected_type}, got {self.current_token.type if self.current_token else 'EOF'}")
        self.current_token = self.lexer.next_token()
