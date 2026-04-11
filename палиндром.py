def is_palindrome(palindrome):
    # Ваш код здесь
    palindrome = str.lower(palindrome)
    new_palindrome = palindrome.replace(' ', '')
    return new_palindrome == new_palindrome[::-1]



# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))

#Требования:
#В решении должны использоваться срезы строк.
#При проверке строки программа должна игнорировать регистр символов и пробелы.