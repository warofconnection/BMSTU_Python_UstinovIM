"""
Главный файл для запуска
"""

from lexer import Lexer
from parser import Parser


def simple_test():
    """Самый простой тест"""
    print("=" * 60)
    print("ПРОСТЕЙШИЙ ТЕСТ ПАРСЕРА")
    print("=" * 60)

    lexer = Lexer()
    parser = Parser()

    # Самый простой код
    test_code = "x = 10;"

    print(f"\nКод: '{test_code}'")

    print("\n1. Лексический анализ:")
    tokens = list(lexer.tokenize(test_code))
    print(f"   Токены:")
    for token in tokens:
        print(f"     {token.name:<10} = '{token.value}'")

    print("\n2. Синтаксический анализ:")
    try:
        # Важно: передаем итератор, не список!
        ast = parser.parse(iter(tokens))
        print("   ✓ УСПЕХ! AST построен")
        print(f"   Корневой узел: {ast}")
        print(f"   Тип: {type(ast).__name__}")
        print(f"   Количество операторов: {len(ast.statements)}")

        print("\n3. Детализация:")
        stmt = ast.statements[0]
        print(f"   Оператор: {stmt}")
        print(f"   Тип оператора: {type(stmt).__name__}")

        if hasattr(stmt, 'name'):
            print(f"   Переменная: {stmt.name}")
        if hasattr(stmt, 'value'):
            print(f"   Значение: {stmt.value}")

    except Exception as e:
        print(f"   ✗ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()


def step_by_step():
    """Пошаговый разбор"""
    print("\n" + "=" * 60)
    print("ПОШАГОВЫЙ РАЗБОР")
    print("=" * 60)

    lexer = Lexer()
    parser = Parser()

    tests = [
        "x = 10;",
        "y = 20;",
        "z = x + y;",
        "a = (2 + 3) * 4;",
    ]

    for code in tests:
        print(f"\n▶ Код: '{code}'")
        try:
            tokens = list(lexer.tokenize(code))
            ast = parser.parse(iter(tokens))
            print(f"   ✓ {ast}")
            print(tokens)
        except Exception as e:
            print(f"   ✗ {e}")


if __name__ == "__main__":
    simple_test()
    step_by_step()