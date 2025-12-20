from rply import ParserGenerator
# Импортируем из ast_nodes вместо ast
from ast_nodes import Program, Assign, BinOp, Number, Name

class Parser:
    def __init__(self):
        # Убираем EQ из списка токенов пока что
        self.pg = ParserGenerator(
            ['NUMBER', 'NAME', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
             'ASSIGN', 'LPAREN', 'RPAREN', 'SEMICOLON'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MULTIPLY', 'DIVIDE']),
            ]
        )

        self._build_parser()
        self.parser = self.pg.build()

    def _build_parser(self):
        @self.pg.production('program : statements')
        def program(p):
            return Program(p[0])

        @self.pg.production('statements : statement')
        def statements_single(p):
            return [p[0]]

        @self.pg.production('statements : statements statement')
        def statements_multiple(p):
            return p[0] + [p[1]]

        @self.pg.production('statement : assign SEMICOLON')
        def statement_assign(p):
            return p[0]

        @self.pg.production('assign : NAME ASSIGN expr')
        def assign(p):
            return Assign(p[0].value, p[2])

        @self.pg.production('expr : expr PLUS expr')
        @self.pg.production('expr : expr MINUS expr')
        @self.pg.production('expr : expr MULTIPLY expr')
        @self.pg.production('expr : expr DIVIDE expr')
        def expr_binop(p):
            return BinOp(p[0], p[1].value, p[2])

        @self.pg.production('expr : LPAREN expr RPAREN')
        def expr_paren(p):
            return p[1]

        @self.pg.production('expr : NUMBER')
        def expr_number(p):
            return Number(int(p[0].value))

        @self.pg.production('expr : NAME')
        def expr_name(p):
            return Name(p[0].value)

        @self.pg.error
        def error_handler(token):
            if token:
                raise SyntaxError(f"Неожиданный токен: {token.name} ('{token.value}')")
            else:
                raise SyntaxError("Неожиданный конец файла")

    def parse(self, tokens):
        return self.parser.parse(tokens)