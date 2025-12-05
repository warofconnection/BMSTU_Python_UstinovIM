from rply import LexerGenerator


class Lexer:

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('STAR', r'\*')
        self.lexer.add('SLASH', r'\/')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('SEMI_COLON', r'\;')

