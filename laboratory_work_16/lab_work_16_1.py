import re

def parse_log_file(filename):
    """
    Извлекает из лог-файла IP-адреса, коды ошибок и метод с URL.
    """
    # Регулярные выражения
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    error_code_pattern = r'\b(?:[1-5][0-9]{2})\b'  # HTTP коды от 100 до 599
    method_url_pattern = r'"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+([^"\s]+)'

    results = {
        'ip_addresses': [],
        'error_codes': [],
        'methods_and_urls': []
    }

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                # Извлечение IP-адресов
                ips = re.findall(ip_pattern, line)
                results['ip_addresses'].extend(ips)

                # Извлечение кодов ошибок
                errors = re.findall(error_code_pattern, line)
                results['error_codes'].extend(errors)

                # Извлечение метода и URL
                method_url_matches = re.findall(method_url_pattern, line)
                for method, url in method_url_matches:
                    results['methods_and_urls'].append((method, url))

        return results

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    # Парсим лог-файл
    data = parse_log_file('input.txt')

    if data:
        # Вывод результатов
        print("=" * 60)
        print("РЕЗУЛЬТАТЫ ПАРСИНГА ЛОГ-ФАЙЛА")
        print("=" * 60)

        print("\nIP-АДРЕСА:")
        if data['ip_addresses']:
            for ip in data['ip_addresses']:
                print(f"  • {ip}")
            print(f"  Всего: {len(data['ip_addresses'])}")

        print("\nКОДЫ ОШИБОК (4xx, 5xx):")
        if data['error_codes']:
            for code in data['error_codes']:
                print(f"  • {code}")
            print(f"  Всего: {len(data['error_codes'])}")
        else:
            print("  Не найдено")

        print("\nМЕТОД И URL:")
        if data['methods_and_urls']:
            for method, url in data['methods_and_urls']:
                print(f"   {method} → {url}")
            print(f"  Всего: {len(data['methods_and_urls'])}")

        # Статистика по методам
        print("\nСТАТИСТИКА ПО МЕТОДАМ:")
        method_count = {}
        for method, _ in data['methods_and_urls']:
            method_count[method] = method_count.get(method, 0) + 1
        for method, count in method_count.items():
            print(f"  {method}: {count}")

if __name__ == "__main__":
    main()