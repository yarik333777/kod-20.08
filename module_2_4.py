numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_primes = True

    for j in range(2, i):

        if i % j != 0:
            is_primes = False
            break

 
        if is_primes:
            primes.append(i)
        else:
            not_primes.append(i)

print(primes)
print(not_primes)



    # Создайте пустые списки primes и not_primes.
    # При помощи цикла for переберите список numbers.
    # Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из превого цикла.
    # Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
    # В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в
    # зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
    # Выведите списки primes и not_primes на экран(в консоль).
    #







# numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in numbers_:
#     if i == 1:
#         continue
#     is_primes = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_primes = False
#             break
#
#         if is_primes:
#             primes.append(i)
#         else:
#             not_primes.append(i)

# print(primes)
# print(not_primes)


# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из превого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в
# зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).
#
# Пример результата выполнения программы:
# Исходный код:
#  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Вывод на консоль:
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]