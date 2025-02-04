
from typing import Optional

class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами.
    Предоставляет методы для чтения, записи и добавления данных в TXT файлы.
    """
    
    def read_file(self, filepath: str) -> str:
        """
        Читает содержимое файла и возвращает его в виде строки.
        
        Args:
            filepath: Путь к файлу для чтения
            
        Returns:
            str: Содержимое файла или пустая строка, если файл не найден
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except PermissionError:
            print(f"Нет прав доступа к файлу {filepath}")
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return ""

    def write_file(self, filepath: str, *data: str) -> None:
        """
        Записывает данные в файл (перезаписывает существующий).
        
        Args:
            filepath: Путь к файлу для записи
            *data: Строки для записи в файл
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for item in data:
                    file.write(str(item))
        except PermissionError:
            print(f"Нет прав доступа для записи в файл {filepath}")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")

    def append_file(self, filepath: str, *data: str) -> None:
        """
        Добавляет данные в конец файла.
        
        Args:
            filepath: Путь к файлу для дополнения
            *data: Строки для добавления в файл
        """
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                for item in data:
                    file.write(str(item))
        except PermissionError:
            print(f"Нет прав доступа для дополнения файла {filepath}")
        except Exception as e:
            print(f"Произошла ошибка при дополнении файла: {e}")
