input_data = input('Напишите в кавычках слова, которые нужно посчитать')
special_char = ('@', '#', '$', '%', '^', '&', '*', '-', '+', '/', '=', '!', '?')

if input_data:
    if input_data.startswith('"') and input_data.endswith('"'):
        words = input_data.replace('"', '')
        words = words.strip()
        words = words.split()
        print(words)
        number_of_words = len(words)
        for word in words:
            if word in special_char:
                number_of_words -= 1
            try:
                if float(word):
                    number_of_words -= 1
                elif int(word):
                    number_of_words -= 1
            except ValueError:  # if it can't convert to number, it's char
                pass
    else:
        print('Вы не написали слова в кавычках')
        number_of_words = 0
else:
    print('Вы ничего не написали')
    number_of_words = 0

print('Количество слов: ', number_of_words)
