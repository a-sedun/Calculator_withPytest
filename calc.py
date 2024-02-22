def dodavannya(x, y):
    return x + y


def vidnimannya(x, y):
    return x - y


def mnozhennya(x, y):
    return x * y


def dilennya(x, y):
    if y != 0:
        return x / y
    else:
        return "Помилка: ділення на нуль"


def cilochislenne_dilennya(x, y):
    if y != 0:
        return x // y
    else:
        return "Помилка: ділення на нуль"


def osta4a_vid_cilochislenogo_dilennya(x, y):
    if y != 0:
        return x % y
    else:
        return "Помилка: ділення на нуль"


print("Оберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Цілочисельне ділення")
print("6. Остача від цілочисельного ділення")

operation = input("Введіть номер операції (1-6): ")

if operation in ("1", "2", "3", "4", "5", "6"):
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))

    if operation == "1":
        print(x, "+", y, "=", dodavannya(x, y))
    elif operation == "2":
        print(x, "-", y, "=", vidnimannya(x, y))
    elif operation == "3":
        print(x, "*", y, "=", mnozhennya(x, y))
    elif operation == "4":
        print(x, "/", y, "=", dilennya(x, y))
    elif operation == "5":
        print(x, "//", y, "=", cilochislenne_dilennya(x, y))
    elif operation == "6":
        print(x, "%", y, "=", osta4a_vid_cilochislenogo_dilennya(x, y))
else:
    print("Невірний вибір операції")
