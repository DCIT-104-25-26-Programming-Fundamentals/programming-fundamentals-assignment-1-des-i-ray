def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


if __name__ == "__main__":
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = []
        for i in range(n):
            value = float(input(f"Enter number {i + 1}: "))
            numbers.append(value)

        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {find_max(numbers)}")
        print(f"Minimum: {find_min(numbers)}")