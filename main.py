


# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5.
#Пример:
#Меньше либо равно пяти: [1, 1, 2, 3, 5]
#Больше пяти: [8, 13, 21, 34, 55, 89]

# a = [1,2,3,4,5,8,13,21,34,55,89]
#
# num = []
# for i in a:
#     if i > 5:
#         num.append(i)
# print(num)
#
# num1 = []
# for i in a:
#     if i <= 5:
#         num1.append(i)
# print(num1)



#Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в соответствующие переменные. Сохраните полученные значения в список.

# name = [input('Введите имя: '),input('Введите фамилия: '),input('Введите возраст: ')]
#
# print(name)



#3. Напишите программу, которая принимает от пользователя секвенцию чисел, разделенных запятой и пробелом. После чего запишите каждое число в список и кортеж.

# nums = input('Введите секвенцию чисел по:", " ')
# list_nums = nums.split(', ')
# print(list_nums)
# list_nums = tuple(list_nums)
# print(list_nums)





#Введите числа: 2, 3, 4, 5, 123, 3, 4, 5, 5678, 3, 4, 53, 2
#Список: [‘2’, ‘3’, ‘4’, ‘5’, ‘123’, ‘3’, ‘4’, ‘5’, ‘5678’, ‘3’, ‘4’, ‘53’, ‘2’].
#Кортеж: (‘2’, ‘3’, ‘4’, ‘5’, ‘123’, ‘3’, ‘4’, ‘5’, ‘5678’, ‘3’, ‘4’, ‘53’, ‘2’)
#4. Напишите программу, которая принимает пример со СЛОЖЕНИЕМ у пользователя и затем выдает результат.
#Пример:
#Введите пример со сложением: 3 + 5 + 5
#13

# cal = input('Введите СЛОЖЕНИЕМ: ')
#
#
# list2 = cal.split('+')
#
# list_num = []
# for i in list2:
#     list_num = list2.append(int(i))
#
# print(list_num)


#**********************************************************************


#5. Напишите программу, которая будет принимать три имени в качестве входных данных от пользователя в одном input() вызове функции.
#Попросите пользователя ввести три имени, разделенных пробелом.
#Разделите входную строку на пробел с помощью split() функции, чтобы получить три отдельных имени



# name = input('Введите три имя через пробель ')
# list_name = name.split(', ')
# print(list_name)







#***************************************************************


#6 *. Дан список чисел. напишите программу, которая превращает каждый элемент списка в его квадрат.
#Дано :
#numbers = [1, 2, 3, 4, 5, 6, 7]
#Ожидаемый результат:
#[1, 4, 9, 16, 25, 36, 49]

# numbers = [1,2,3,4,5,6,7]
#
# for i in numbers:
#     print(i ** 2)




