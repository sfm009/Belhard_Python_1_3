"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На вход функции подается текст, содержащий дополнения в скобках
Например:
Функции Python (интерпретируемый язык программирования с динамической типизацией данных) необходимы
для выделения и повторного использования фрагментов кода.

Необходмо разработать функцию, которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст

При разработке алгоритма решения нужно учесть, что скобки могут быть вложенные, и  что самая последняя открывающая
скобка должна обязательно иметь после себя закрывающую. Результат не должен содержать в пробелов в начале и в конце текста.

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'Опять (лишний фрагмент) программировать' -> 'Опять программировать'
- 'Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)' -> 'Падал прошлогодний снег'
"""


def shortener(text):
    words = string.split(' ')
    fragment_1 = '('
    fragment_2 = ')'
    new_words = []
    for word in words:
        if fragment_1 not in word and fragment_2 not in word:
            new_words.append(word)
    result = ' '.join(new_words)
    return result


if __name__ == '__main__':
    string = input('Введите строку для очистки: ')
    print(f"Чистый текст: {shortener(string)}")
