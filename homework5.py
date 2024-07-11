#2. Задайте переменные разных типов данных:
# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (1, 2.5, 'string', False)
# - Выполните операции вывода кортежа immutable_var на экран.
print('Значение кортежа immutable_var: ',immutable_var)
#3. Изменение значений переменных:
#  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#immutable_var[0] = 5 - ошибка: TypeError: 'tuple' object does not support item assignment, так как нельзя изменять неизменяемые элементы кортежа
#4. Создание изменяемых структур данных:
#  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 2.5, 'string', False]
print('Значение списка mutable_list: ', mutable_list)
#  - Измените элементы списка mutable_list.
mutable_list.append('список')
mutable_list[2] = 'изменяемый'
mutable_list.remove(False)
#  - Выведите на экран измененный список mutable_list.
print('Значение измененного списка mutable_list: ', mutable_list)