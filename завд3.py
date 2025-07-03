import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізуємо colorama
init()

def print_tree(path: Path, prefix=""):
    if path.is_dir():
        print(prefix + Fore.BLUE + path.name + "/" + Style.RESET_ALL)
        for child in sorted(path.iterdir()):
            print_tree(child, prefix + "    ")
    else:
        print(prefix + Fore.GREEN + path.name + Style.RESET_ALL)

def main():
    if len(sys.argv) < 2:
        print("Помилка: не вказано шлях до директорії.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Помилка: вказаний шлях не існує.")
        return

    if not directory.is_dir():
        print("Помилка: вказаний шлях не є директорією.")
        return

    print_tree(directory)

if __name__ == "__main__":
    main()
