"""Модуль для шифрования и расшифровки текста шифром Цезаря."""


class CipherMaster:
    """Класс для шифрования и расшифровки текста русским алфавитом."""

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        """
        Обрабатывает текст: шифрует или расшифровывает с заданным сдвигом.

        Args:
            text: Исходный текст для обработки.
            shift: Величина сдвига.
            is_encrypt: True для шифрования, False для расшифровки.

        Returns:
            str: Обработанный текст.
        """
        result = []

        if not is_encrypt:
            shift = -shift

        for letter in text:
            if letter.lower() in self.alphabet:
                # Находим индекс буквы в алфавите (приводим к нижнему регистру)
                index = self.alphabet.find(letter.lower())
                # Вычисляем новый индекс с учетом сдвига и зацикливания
                new_index = (index + shift) % len(self.alphabet)
                # Берем новую букву (всегда в нижнем регистре)
                new_letter = self.alphabet[new_index]
                result.append(new_letter)
            else:
                # Если символ не из алфавита (пробел, знаки препинания),
                # оставляем как есть
                result.append(letter)
        return ''.join(result)


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
