import re
from typing import Callable


def generator_numbers(text: str):
    """Генератор, который находит все целые числа в тексте и возвращает их по очереди."""
    for match in re.findall(r'\b\d+\.\d+\b', text):  # Знаходимо всі цілі числа
        yield float(match)  # Повертаємо їх у вигляді int


def sum_profit(text: str, func: Callable[[str], float]) -> float:
    """Обсчитывает общую сумму целых чисел, найденных в тексте."""
    return sum(func(text))  # Викликає generator_numbers і підсумовує числа


def main():
    # Приклад використання:
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_profit = sum_profit(text, generator_numbers)
    # Очікуваний результат:
    print(f"Загальний прибуток: {total_profit:.2f}")


if __name__ == "__main__":
    main()
