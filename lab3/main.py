# #Task 1
# s = "YYYYggkeeeAAABV"
# res = ""
# count = 1
# for i in range(0, len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         res += s[i]
#         if count != 1:
#             res += str(count)
#         count = 1
#     if i + 1 == len(s) - 1:
#         res += s[i + 1]
#         if count != 1:
#             res += str(count)
# print(res)

# #Task 2
# s = "Y4g2ke3A3BV"
# res = ""
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         res += s[i]
#         temp = s[i]
#     if s[i].isdigit():
#         count = ''
#         count += s[i]
#         res += temp * (int(count)-1)
#
# print(res)


# # Task 3
# Словари для преобразования чисел в текст
# units = {
#     1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
#     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
# }
#
# teens = {
#     10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#     14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#     17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'
# }
#
# tens = {
#     2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
#     6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
# }
#
# hundreds = {
#     1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот',
#     6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'
# }
#
# number = int(input("Введите число от 1 до 1000: "))
#
# if 1 <= number <= 1000:
#     # Определение единиц, десятков и сотен
#     hundreds_digit = number // 100
#     tens_digit = (number % 100) // 10
#     units_digit = number % 10
#
#     # Вывод числового представления текстом
#     if hundreds_digit > 0:
#         print(hundreds[hundreds_digit], end=' ')
#     if tens_digit == 1:
#         print(teens[number % 100])
#     else:
#         if tens_digit > 0:
#             print(tens[tens_digit], end=' ')
#         if units_digit > 0:
#             print(units[units_digit])
# else:
#     print("Введите число в диапазоне от 1 до 1000.")

# # Task 4
# strings = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
# empty_arr = {}
#
# for string in strings:
#     if string in empty_arr:
#         empty_arr[string] += 1
#     else:
#         empty_arr[string] = 1
#
# for string, count in empty_arr.items():
#     print(count, end=' ')

# # Task 5
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]]
#
#
# det = (mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) -
#        mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) +
#        mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))
#
#
# if det == 0:
#     print(f"Определитель матрицы равен: {det} => столбцы линейно зависимы")
#
# else:
#     print(f"Определитель матрицы равен: {det} => столбцы линейно независимы")
#     print(mat)

# # Task 6
n = input("Введите строку: ")

words = n.split()
abbreviation = ""
for word in words:
    abbreviation += word[0].upper()

print("Аббревиатура:", abbreviation)

