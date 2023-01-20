from math import sqrt


def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif len(phrase) <= 3 or len(phrase[:size]) <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'


def mango(quantity, price):
    return (quantity - quantity // 3) * price


def unique_in_order(sequence):
    output = []
    if len(sequence) == 0:
        return output
    elif len(sequence) == 1:
        output.append(sequence[0])
        return output
    else:
        for i in range(len(sequence)):
            if i == 0:
                output.append(sequence[i])
            elif i == len(sequence) - 1:
                if sequence[i] != sequence[i - 1]:
                    output.append(sequence[i])
            else:
                if sequence[i - 1] != sequence[i] and sequence[i + 1]:
                    output.append(sequence[i])
        return output


def is_square(n: int) -> True or False:
    if n >= 0:
        if n == 0:
            return True
        elif sqrt(n) == int(sqrt(n)):
            return True
        else:
            return False
    else:
        return False


def likes(names: list) -> str:
    if names == []:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


# print(trim("Hello, world!", 8))
# print(mango(9, 5))
# print(unique_in_order("ABBCcA"))
# print(is_square(26))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))