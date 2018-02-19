str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')

if str1 == str2:
	print('1')
elif str1 != str2 and str2 == 'learn':
	print('3')	
elif str1 != str2 and len(str1) > len(str2):
	print('2')
