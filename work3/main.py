import sys
import re


def parse_logs(line):
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(pattern, line)
    if match:
        return {"timestamp": match.group(1), "level": match.group(2), "message": match.group(3)}
    print(f"Помилка: Не вдалося розібрати рядок: {line}")
    return None


def open_file_logs(file_path):
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                log = parse_logs(line.strip())
                if log:
                    logs.append(log)
    except Exception as e:
        print(f"Помилка при відкритті файлу: {e}")
    return logs


def log_level(logs, level):
    return [log for log in logs if log["level"] == level.upper()]


def sorted_logs(logs):
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts


def paint_log(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def paint_details(logs):
    print("\nДеталі логів:")
    for log in logs:
        print(f"{log['timestamp']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Помилка: Вкажіть шлях до файлу логів")
        return

    logs = open_file_logs(sys.argv[1])
    if not logs:
        print("Файл не містить валідних логів або порожній")
        return

    counts = sorted_logs(logs)
    paint_log(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered_logs = log_level(logs, level)
        if filtered_logs:
            paint_details(filtered_logs)
        else:
            print(f"Логів для рівня '{level}' не знайдено")


if __name__ == "__main__":
    main()
