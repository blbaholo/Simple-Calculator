def add(*numbers) -> float:
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(*numbers) -> float:
    total = 1
    for number in numbers:
        total *= number
    return total
