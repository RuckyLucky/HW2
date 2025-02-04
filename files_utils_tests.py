
from files_utils import *

# Тестовые данные
test_json_data = [
    {"name": "Иван", "age": 25},
    {"name": "Мария", "age": 23}
]

test_csv_data = [
    {"имя": "Иван", "возраст": "25", "город": "Москва"},
    {"имя": "Мария", "возраст": "23", "город": "Санкт-Петербург"}
]

test_txt_data = "Это тестовая строка\nДля проверки работы с текстовым файлом"

test_yaml_data = """
weather_app:
  api_key: abc123
  units: metric
  language: ru
  cities:
    - Moscow
    - Saint Petersburg
  update_interval: 30
"""

# Тестирование JSON функций
write_json(test_json_data, "test.json")
print("JSON прочитан:", read_json("test.json"))
append_json([{"name": "Петр", "age": 30}], "test.json")

# Тестирование CSV функций
write_csv(test_csv_data, "test.csv")
print("CSV прочитан:", read_csv("test.csv"))
append_csv([{"имя": "Петр", "возраст": "30", "город": "Казань"}], "test.csv")

# Тестирование TXT функций
write_txt(test_txt_data, "test.txt")
print("TXT прочитан:", read_txt("test.txt"))
append_txt("\nДобавленная строка", "test.txt")

# Тестирование YAML
with open("test.yaml", "w", encoding="utf-8") as f:
    f.write(test_yaml_data)
print("YAML прочитан:", read_yaml("test.yaml"))
