import sys
from parser import get_format_logs
from data_processing import count_logs_by_level, display_log_counts, filter_logs_by_level


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = get_format_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Немає записів для рівня '{level_filter.upper()}'.")


if __name__ == "__main__":
    main()
