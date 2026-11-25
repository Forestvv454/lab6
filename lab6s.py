# Функция ввода данных
def input_data():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    return start, end


# Проверка числа на простоту
def IsPrime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Поиск следующего простого числа
def NextPrime(number):
    number += 1

    while not IsPrime(number):
        number += 1

    return number


# Поиск простых чисел в диапазоне
def PrimeRange(start, end):
    primes = []

    for number in range(start, end + 1):
        if IsPrime(number):
            primes.append(number)

    return primes


# Функция вывода результата
def output_data(primes, end):
    print("Простые числа в диапазоне:", primes)
    print("Следующее простое число после", end, ":", NextPrime(end))


# Основная часть программы
start, end = input_data()
primes = PrimeRange(start, end)
output_data(primes, end)