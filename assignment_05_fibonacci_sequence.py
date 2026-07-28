def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_fibonacci(number):
    if number < 0:
        return False

    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False


if __name__ == "__main__":
    # ---------------- PART A: First N Terms ----------------
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        sequence = generate_fibonacci(n)
        print("Fibonacci sequence:", " ".join(map(str, sequence)))

    # ---------------- PART B: Check Membership ----------------
    number = int(input("\nEnter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")