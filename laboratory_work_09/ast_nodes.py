"""
AST узлы для MiniPython
"""


class Node:
    def __repr__(self):
        attrs = []
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                attrs.append(f"{key}={repr(value)}")

        if attrs:
            return f"{self.__class__.__name__}({', '.join(attrs)})"
        return f"{self.__class__.__name__}()"


class Program(Node):
    def __init__(self, statements):
        self.statements = statements


class Assign(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Number(Node):
    def __init__(self, value):
        self.value = value


class Name(Node):
    def __init__(self, id):
        self.id = id