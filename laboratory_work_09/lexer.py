from rply import LexerGenerator

class Lexer:
    def __init__(self):
        self.lexer = self._build_lexer()

    def _build_lexer(self):
        lg = LexerGenerator()

        lg.add('NUMBER', r'\d+')
        lg.add('NAME', r'[a-zA-Z_][a-zA-Z0-9_]*')
        lg.add('PLUS', r'\+')
        lg.add('MINUS', r'-')
        lg.add('MULTIPLY', r'\*')
        lg.add('DIVIDE', r'\/')
        lg.add('ASSIGN', r'=')
        lg.add('LPAREN', r'\(')
        lg.add('RPAREN', r'\)')
        lg.add('SEMICOLON', r';')

        lg.ignore(r'\s+')

        return lg.build()

    def tokenize(self, text):
        return self.lexer.lex(text)
