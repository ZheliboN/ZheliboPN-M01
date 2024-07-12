#Организуйте программу:
#Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
my_string = input('Введите строку: ')
#Вывести количество символов введённого текста
#Определение длины строки
count_symbol = len(my_string)
print('Количество символов введенного текста:', count_symbol)
#3. Работа с методами строк:
#Используя методы строк, выполните следующие действия:
#Выведите строку my_string в верхнем регистре.
print('Строка в верхнем регистре:', my_string.upper())
#Выведите строку my_string в нижнем регистре.
print('Строка в нижнем регистре:', my_string.lower())
#Измените строку my_string, удалив все пробелы.
#Верно ли указано задание: изменить исходную строку или вывести  с удаленными пробелами?)
print('Вывод строки без пробелов:', my_string.replace(' ',''))
#Есле все таки "изменить", то значит присваиваем новое значение, но теряем исходное значение строки:
my_string = my_string.replace(' ','')
#Вывод строки без пробелов
print('Измененная строка без пробелов:', my_string)
#Выведите первый символ строки my_string.
print('Первый символ строки:', my_string[0])
#Выведите последний символ строки my_string.
#Определение длины строки после удаления пробелов
count_symbol = len(my_string)
print('Последний символ строки:', my_string[count_symbol-1])
print('Количество символов введенного текста после удаления пробелов:', count_symbol)
#Примечания:
#Для вывода значений на экран используйте функцию print().
#Для вызова методов строк используйте операцию точки '.'.