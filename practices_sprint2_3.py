class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in original_text:
            if letter.lower() in self.alphabet:
                # Находим индекс буквы в алфавите (приводим к нижнему регистру)
                index = self.alphabet.find(letter.lower())
                # Вычисляем новый индекс с учетом сдвига и зацикливания
                new_index = (index + shift) % len(self.alphabet)
                # Берем новую букву (всегда в нижнем регистре)
                new_letter = self.alphabet[new_index]
                result.append(new_letter)
            else:
                # Если символ не из алфавита (пробел, знаки препинания), оставляем как есть
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.find(letter.lower())
                # Для расшифровки сдвиг берется с обратным знаком
                new_index = (index - shift) % len(self.alphabet)
                new_letter = self.alphabet[new_index]
                result.append(new_letter)
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Пришло ревью в шифрованном виде. Кажется, нас расскрыли!',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
