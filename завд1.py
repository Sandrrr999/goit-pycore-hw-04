def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        continue  
            average = total // count if count else 0
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0