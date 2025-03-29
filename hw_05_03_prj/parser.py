import re
from loaddata import load_data


def parse_log_line(line: str) -> dict:
    """Розбирає рядок логу та повертає словник з компонентами: дата, час, рівень, повідомлення."""
    match = re.match(r'(\S+) (\S+) (\S+) (.+)', line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return None


def get_format_logs(file_path: str) -> list[dict]:
    """ Розбирає та перетворює всі логи в список словників."""
    # load_data(file_path) -> list of lines in log
    # [new_item for item in iterable if condition]
    # map(function, iterable, ...) !!!Ok
    return list(map(lambda line: parse_log_line(line.rstrip()), load_data(file_path)))
