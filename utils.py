def find_max(numbers):
    max_nbr = numbers[0]
    for value in numbers:
        if value > max_nbr:
            max_nbr = value
    return max_nbr