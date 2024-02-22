# calculator.py
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
