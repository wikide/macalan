try:
	macalan_year = int(input('Макалан какой выдержи нужно получить из макалана 3 и 12 ? '))
except ValueError:
	exit('Нужное ввести целое число от 3 до 12')

if int(macalan_year) < 3:
	exit('Нужно значение большее или равное 3')
elif int(macalan_year) > 12:
	exit('Нужно значение меньшее или равное 12')

print('Для того чтобы макалан был выдержки ' + str(macalan_year) + ' лет')
print('Нужно смешать макалан 3 лет и Макалан 12 лет в соотношении: ' + str(round(float((12-macalan_year)/3),2)) + ' к 1')
