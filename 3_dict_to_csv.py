"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    list_dict = [
        {'name':'Уасилий','age':'23','job':'ассенизатор'},
        {'name':'Олег','age':'50','job':'бумер'},
        {'name':'Ярослав','age':'41','job':'великий князь киевский'},
        {'name':'Златан','age':'18','job':'конокрад'}
    ]

    with open(u'C:/Users/bezre/OneDrive/Desktop/myprojexts/pyschooltasks/day2/learn-homework-2/ppl.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['name','age','job']
        for item in list_dict:
            writer = csv.DictWriter(file, fieldnames = fieldnames )
            writer.writerow(item)


if __name__ == "__main__":
    main()
