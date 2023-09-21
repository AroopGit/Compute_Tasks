def print_hollow_pyramid(n):
    for i in range(n):
        for j in range(2 * n - 1):
            if i == n - 1 or i + j == n - 1 or j - i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

try:
    n = int(input("Enter the number of rows for the hollow pyramid: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print_hollow_pyramid(n)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
