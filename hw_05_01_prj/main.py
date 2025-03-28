import time


def caching_fibonacci():
    cache = {}  # створюємо кеш словник

    def fibonacci(n):
        if n in cache:  # Перевіряємо, чи є значення в кеші
            return cache[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n -
                                                    2)  # Обчислюємо і кешуємо
            return cache[n]
    return fibonacci  # Повертаємо внутрішню функцію


def un_caching_fibonacci():
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci  # Повертаємо внутрішню функцію

# порахуємо час виконання функціі, та порівняємо, чому ні?:


def measure_time(func, n):
    start_time = time.perf_counter()  # Початок високоточного таймера
    result = func(n)  # Виконання функції
    end_time = time.perf_counter()  # Кінець високоточного таймера
    execution_time = end_time - start_time  # Обчислення часу виконання
    print(
        f"Fibonacci({n}) = {result}, виконано за {execution_time:.6f} секунд")


def main():
    fib_cashed = caching_fibonacci()
    fib_uncashed = un_caching_fibonacci()
    print('Cashed:')
    measure_time(fib_cashed, 10)
    measure_time(fib_cashed, 15)
    measure_time(fib_cashed, 30)
    measure_time(fib_cashed, 35)

    print('\nUnCashed:')
    measure_time(fib_uncashed, 10)
    measure_time(fib_uncashed, 15)
    measure_time(fib_uncashed, 30)
    measure_time(fib_uncashed, 35)

    # fib = caching_fibonacci()
    # print(fib(10))  # 55
    # print(fib(15))  # 610


if __name__ == "__main__":
    main()
