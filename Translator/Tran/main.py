import random
from os import system, name
from time import sleep

def clear():
   if name == 'nt':
      _ = system('cls')

randau = random.randint(0, 1)

if randau:
    print("Русско-Бабиджонский переводчик by Tima#5732 & Tim#8661")
else:
    print("Русско-Бабиджонский переводчик by Tim#8661 & Tima#5732")

sleep(2)
clear()
    
print("Выбор режима:",
      "Если вы хотите перевести с Русского на Бабиджонский введите 1",
      "Если вы хотите перевести с Бабиджонского на Русский введите 2",
      sep='\n')

x = input("Режим: ")

clear()

if x == '1':
    d = dict([])
    lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '?',
            '!', '&lt;', '&gt;', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '&amp;', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']
    lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ', ', '.', '?',
            '!', '&lt;', '&gt;', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '&amp;', '(', ')','-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']

    seed = ''
    i = 0
    while (len(lst2)):
        x = random.randint(0, len(lst2) - 1)
        seed += str(x) + ' '
        d[lst1[i]] = lst2[x]
        lst2.pop(x)
        i += 1
    print("Введите сообщение:")
    st = input()
    print("Ваш ключ и сообщение:")
    print(seed)
    for i in st:
        print(d[i], end='')
elif x == '2':
    d = dict([])
    lst1 = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ', ', '.', '?',
            '!', '&lt;', '&gt;', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '&amp;', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']
    lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В',
            'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
            'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в',
            'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
            'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', ', ', '.', '?',
            '!', '&lt;', '&gt;', '`', '~', "'", '"', '@', '№', '#',
            ';', '$', '%', '^', ':', '&amp;', '(', ')', '-', '_', '+',
            '=', '*', '/', '\\', '|', '{', '}', '[', ']']

    print("Введите ключ и сообщение")
    seed = input()
    st = input()
    i = 0
    n = ''
    output = ''
    print()
    for x in seed:
        if x == ' ':
            d[lst2[int(n)]] = lst1[i]
            lst2.pop(int(n))
            i += 1
            n = ''
        else:
            n += x
    for i in st:
        output += d[i]
    print()
    print(output)
else:
    print('Ты еблан')

print()
print()
print("Перевод завершен")
print("Программа закроется через 10 секунд")
sleep(10)