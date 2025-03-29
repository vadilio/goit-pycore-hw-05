from collections import Counter


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фильтрує логи (logs: list[dict]) по вказаному рівню (level: str) -> list[dict]
    На вході список словників всіх логов, на виході список словників вказаного рівня
    """
    # або так:
    # return [log for log in logs if log['level'].upper() == level.upper()]
    # обо так:
    return list(filter(lambda log: log['level'] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів для кожного рівня логування."""
    return Counter(log['level'] for log in logs)


def display_log_counts(counts: dict):
    """Виводить статистику за рівнями логування у форматі таблиці."""
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<8}")
