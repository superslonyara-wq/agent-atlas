"""Показывает профиль ученика из файла data/profile.json.

Запуск из корня проекта:
    python3 scripts/show_profile.py
"""

import json
from pathlib import Path

# Путь к профилю считаем от расположения этого скрипта,
# чтобы скрипт работал из любой текущей папки.
PROFILE_PATH = Path(__file__).resolve().parent.parent / "data" / "profile.json"

# Понятные подписи для каждого поля профиля.
LABELS = {
    "goal": "Цель",
    "experience": "Опыт",
    "minutes_per_day": "Время в день (минут)",
    "learning_language": "Язык обучения",
}


def load_profile(path=PROFILE_PATH):
    """Читает JSON-файл профиля и возвращает его как словарь."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def main():
    profile = load_profile()
    print("Профиль Agent Atlas")
    print("-" * 20)
    # Выводим поля в том порядке, в каком они перечислены в LABELS.
    for key, label in LABELS.items():
        print(f"{label}: {profile.get(key, 'не указано')}")


# Этот блок срабатывает только при прямом запуске файла,
# а не при импорте его из другого кода (например, из тестов).
if __name__ == "__main__":
    main()
