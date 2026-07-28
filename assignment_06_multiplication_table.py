def print_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number:2} x {i:2} = {number * i}")


def print_tables_up_to(n):
    for number in range(1, n + 1):
        print_table(number)
        print("-" * 27)


if __name__ == "__main__":
    # ---------------- PART A: Single Table ----------------
    num = int(input("Enter a number: "))

    if num <= 0:
        print("Error: Number must be a positive integer.")
    else:
        print_table(num)

    # ---------------- PART B: Tables from 1 to N ----------------
    n = int(input("\nEnter N (to print tables from 1 to N): "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to(n)