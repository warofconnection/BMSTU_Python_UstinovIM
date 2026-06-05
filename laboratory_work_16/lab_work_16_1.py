import re

# Читаем файл
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Регулярные выражения
ip_pattern = r'^(?:\d{1,3}\.){3}\d{1,3}$'
error_pattern = r'^[1-5][0-9]{2,3}$'
method_url_pattern = r'"(GET|POST|PUT|DELETE)\s+([^"\s]+)'

# Списки для результатов
ips = []
errors = []
methods_urls = []

# Обрабатываем каждую строку
for line in lines:
    found_methods = re.findall(method_url_pattern, line)
    for method, url in found_methods:
        methods_urls.append(method + " " + url)
    parts = line.split()
    for part in parts:
        found_ips = re.match(ip_pattern, part, flags=0)
        if found_ips != None:
            ips.append(found_ips.group(0))

        found_errors = re.match(error_pattern, part, flags=0)
        if found_errors != None:
            errors.append(found_errors.group(0))

#
#     # Ищем метод и URL
#     found_methods = re.findall(method_url_pattern, line)
#     for method, url in found_methods:
#         methods_urls.append(method + " " + url)
#
# Выводим результаты
print("IP-адреса:")
for ip in ips:
    print(ip)
#
print("\nКоды ошибок:")
for error in errors:
    print(error)

print("\nМетод и URL:")
for item in methods_urls:
    print(item)