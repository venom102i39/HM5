"""
Інтроспекція бібліотеки colorama
Автор: (Твоє ім'я)
Опис: Встановлення, аналіз структури, вивід важливих атрибутів і методів.
"""

# --- 1. Встановлення бібліотеки (виконується один раз у терміналі) ---
# pip install colorama

# --- 2. Імпорт бібліотек ---
import colorama
import inspect

# --- 3. Інтроспекція модуля colorama ---

print("===== DIR(colorama) - список атрибутів модуля =====")
print(dir(colorama))

print("\n===== Інформація через inspect.getmembers() =====")
for name, obj in inspect.getmembers(colorama):
    print(f"{name} -> {obj}")

# --- 4. Виділення найважливіших атрибутів і методів ---

print("\n===== Найважливіші компоненти: Fore, Back, Style, init =====")

from colorama import Fore, Back, Style, init

print("\n--- Атрибути Fore (кольори тексту) ---")
print(dir(Fore))

print("\n--- Атрибути Back (кольори фону) ---")
print(dir(Back))

print("\n--- Атрибути Style (стилі тексту) ---")
print(dir(Style))

# --- 5. Приклад роботи colorama ---

print("\n===== Приклад роботи colorama =====")

init()  # Активує підтримку ANSI-кодів для Windows

print(Fore.GREEN + "Це зелений текст")
print(Back.YELLOW + "Текст з жовтим фоном")
print(Style.BRIGHT + "Яскравий стиль тексту")
print(Style.RESET_ALL + "Стиль повернуто до стандартного")

# --- 6. Коментарі (висновки) ---
"""
Висновки:

1. init() – найважливіший метод, який включає коректну роботу кольорів у Windows.
2. Fore – набір кольорів тексту (RED, GREEN, BLUE, CYAN, MAGENTA тощо).
3. Back – набір кольорів фону.
4. Style – стилі тексту: BRIGHT, DIM, NORMAL, RESET_ALL.
5. Через функції dir() та inspect.getmembers() можна переглянути всю структуру модуля.
6. Найчастіше програміст використовує комбінацію:
   init(), Fore.<color>, Back.<color>, Style.<style>
7. Colorama простий і корисний модуль, який дозволяє красиво форматувати вивід у консолі.

Цей файл можна завантажувати на GitHub як звіт та демонстрацію інтроспекції модуля.
"""
