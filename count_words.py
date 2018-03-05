amount = 0
with open('referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        amount += len(line_list)

print('Количество слов в файле: ', amount)
