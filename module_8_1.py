# Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        result = round(a + b, 4)
        return result
    except TypeError:
        if isinstance(a, str) and not isinstance(b, str):
            result = a + str(b)
            return result
        elif not isinstance(a, str) and isinstance(b, str):
            result = str(a)+b
            return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))