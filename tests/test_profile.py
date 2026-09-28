"""Проверяет, что файл data/profile.json заполнен правильно.

Запуск из корня проекта:
    python3 -m unittest discover tests
"""

import sys
import unittest
from pathlib import Path

# Добавляем папку scripts в путь поиска модулей,
# чтобы импортировать из неё функцию чтения профиля.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from show_profile import load_profile  # noqa: E402


class ProfileTest(unittest.TestCase):
    def setUp(self):
        # Перед каждой проверкой заново читаем профиль.
        self.profile = load_profile()

    def test_all_fields_present(self):
        # В профиле должны быть все четыре обязательных поля.
        for key in ("goal", "experience", "minutes_per_day", "learning_language"):
            self.assertIn(key, self.profile)

    def test_text_fields_not_empty(self):
        # Текстовые поля не должны быть пустыми строками.
        for key in ("goal", "experience", "learning_language"):
            self.assertTrue(self.profile[key].strip(), f"Поле {key} пустое")

    def test_minutes_per_day(self):
        # Время в день — целое число минут, по условию 180.
        self.assertEqual(self.profile["minutes_per_day"], 180)


if __name__ == "__main__":
    unittest.main()
