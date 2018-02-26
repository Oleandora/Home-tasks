oper_tuple = ('+','-', '/', '*')
evaluation = input(': ')

def calc(a, b, oper):
    try:
        a, b = float(a), float(b)
    except ValueError:
        print('Некорректный ввод, нет одного или двух чисел')    
    try:
        op = {'+': (a+b), '-': (a-b),
              '*': (a*b), '/': (a/b)}
        result = op[oper]
        return result
    except ZeroDivisionError:
        print('Ай-яй-яй! Деление на ноль!')
    

if evaluation.endswith('='):
    evaluation = evaluation.strip().replace('=','')
    f = 1
    for operation in oper_tuple:
        if evaluation.find(operation) != -1:
            a, b = evaluation.split(operation)
            print(calc(a, b, operation))
            f = 0
            break    
    if f:
        print('Нет математического оператора')
    
else:
    print('Некорректный ввод, нет знака "="')