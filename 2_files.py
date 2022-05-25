"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    list = []
    with open(u'C:/Users/bezre/OneDrive/Desktop/myprojexts/pyschooltasks/day2/learn-homework-2/referat.txt','r', encoding= 'utf-8' ) as source:
        for symbol in source:
            list.append(symbol)
    symbol_string = ' '.join(list)
    print(len(symbol_string))
    print(len(symbol_string.split(' ')))
    with open(u'C:/Users/bezre/OneDrive/Desktop/myprojexts/pyschooltasks/day2/learn-homework-2/referat2.txt','a', encoding= 'utf-8' ) as file_2:
        file_2.write(symbol_string.replace('.','!'))

if __name__ == "__main__":
    main()
