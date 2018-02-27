def calculate(operand1, operand2, sign):
    try:
        operand1, operand2 = float(operand1), float(operand2)
        calculation = {'+': lambda x, y: x + y,
                       '-': lambda x, y: x - y,
                       '*': lambda x, y: x * y,
                       '/': lambda x, y: x / y}
        result = calculation[sign](operand1, operand2)
        return result
    except ValueError as e:
        return 'Некорректный ввод, нет одного или двух чисел: {}'.format(e.args[0])
    except ZeroDivisionError as e:
        return 'Ай-яй-яй! Деление на ноль! Фу быть таким!: {}'.format(e.args[0])


if __name__ == '__main__':

    sign_tuple = ('+', '-', '/', '*')
    evaluation = input('Введите математическое выражение со знаком "=" в конце: ')

    if evaluation.endswith('='):
        evaluation = evaluation.strip().replace('=','')
        for operation in sign_tuple:
            if operation in evaluation:
                operand1, operand2 = evaluation.split(operation)
                print(calculate(operand1, operand2, operation))
                break
        else:
            print('Нет математического оператора')
    else:
        print('Некорректный ввод, нет знака "="')