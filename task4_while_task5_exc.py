persons = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
	for i, person in enumerate(persons):
		while person in name:
			print('{0} нашёлся!'.format(persons.pop(i)))
			break
	print('{0} не найден'.format(name))		

def ask_user():

	print('\nПривет!')
	while True:
		try:
			answer = input('Как дела? ')
			answer = answer.lower()
			if answer == 'хорошо':
				break
		except KeyboardInterrupt:
			print('\nПока!')
			break

	get_answer()

def get_answer():

	words_to_answer = {"привет": "И тебе привет!", 
	"как дела?": "Лучше всех.", "пока": "Увидимся!"}

	while True:
		try:
			question = input('Напиши что-нибудь: ')
		
			if isinstance(question, int) or isinstance(question, float):
				print("Вы ввели число, я не смогу ответить")
			else:
				answer = words_to_answer.get(question)

				if answer == 'None':
					print('Не знаю, что на это ответить.')	
				elif question == 'пока':
					print(answer)
					break
				print(answer)

		except KeyboardInterrupt:
			print('\nПока!')
			break

a = input('Введите имя: ')
find_person(a)
ask_user()


