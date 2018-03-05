import csv

words_to_answer = {"привет": "И тебе привет!", "как дела?": "Лучше всех.", "что нового?": "Пока ничего.",
                   "пока": "Увидимся!"}

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['ввод', 'вывод']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for key, value in words_to_answer.items():
        writer.writerow({fields[0]: key, fields[1]: value})
