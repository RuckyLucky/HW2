
"""
Модуль для сжатия изображений с использованием ООП подхода
"""

import os
from typing import Union, Tuple
from PIL import Image
from pillow_heif import register_heif_opener


class ImageCompressor:
    """Класс для сжатия изображений в формат HEIF"""
    
    # Атрибут класса с поддерживаемыми форматами
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')

    def __init__(self, quality: int = 50) -> None:
        """
        Инициализация компрессора изображений
        
        Args:
            quality: Качество сжатия от 0 до 100
        """
        self.__quality = self.__validate_quality(quality)
        register_heif_opener()

    def __validate_quality(self, quality: int) -> int:
        """Валидация значения качества"""
        if not isinstance(quality, int):
            raise TypeError("Качество должно быть целым числом")
        if not 0 <= quality <= 100:
            raise ValueError("Качество должно быть от 0 до 100")
        return quality

    @property
    def quality(self) -> int:
        """Геттер для получения значения качества"""
        return self.__quality

    @quality.setter 
    def quality(self, value: int) -> None:
        """Сеттер для установки значения качества"""
        self.__quality = self.__validate_quality(value)

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение в формат HEIF
        
        Args:
            input_path: Путь к исходному файлу
            output_path: Путь для сохранения
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")

    def process_directory(self, directory: str) -> None:
        """
        Обработка всех поддерживаемых изображений в директории
        
        Args:
            directory: Путь к директории
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)


def main() -> None:
    """Основная функция программы"""
    
    # Создаем экземпляр компрессора
    compressor = ImageCompressor(quality=50)
    
    # Получаем путь от пользователя
    input_path = input("Введите путь к файлу или директории: ").strip('"')

    if not os.path.exists(input_path):
        print("Указанный путь не существует")
        return

    if os.path.isfile(input_path):
        print(f"Обрабатываем файл: {input_path}")
        output_path = os.path.splitext(input_path)[0] + '.heic'
        compressor.compress_image(input_path, output_path)
    else:
        print(f"Обрабатываем директорию: {input_path}")
        compressor.process_directory(input_path)


if __name__ == "__main__":
    main()
