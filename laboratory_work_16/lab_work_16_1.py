import re

# Читаем файл
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Регулярные выражения
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
error_pattern = r'\b[1-5][0-9]{2}\b'
method_url_pattern = r'"(GET|POST|PUT|DELETE)\s+([^"\s]+)'

# Списки для результатов
ips = []
errors = []
methods_urls = []

# Обрабатываем каждую строку
for line in lines:
    # Ищем IP
    found_ips = re.findall(ip_pattern, line)
    for ip in found_ips:
        ips.append(ip)

    # Ищем коды ошибок
    found_errors = re.findall(error_pattern, line)
    for error in found_errors:
        errors.append(error)

    # Ищем метод и URL
    found_methods = re.findall(method_url_pattern, line)
    for method, url in found_methods:
        methods_urls.append(method + " " + url)

# Выводим результаты
print("IP-адреса:")
for ip in ips:
    print(ip)

print("\nКоды ошибок:")
for error in errors:
    print(error)

print("\nМетод и URL:")
for item in methods_urls:
    print(item)