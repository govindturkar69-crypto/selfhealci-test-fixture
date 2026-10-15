def divide(a, b):  # Fix: Change multiplication to division
    return a / b


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


if __name__ == "__main__":
    print(divide(10, 2))
