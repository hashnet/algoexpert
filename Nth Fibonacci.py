def getNthFib(n):
    if n < 2:
        return 0

    num1 = 0
    num2 = 1

    for i in range(2, n):
        num1 = num1 + num2
        num2, num1 = num1, num2

    return num2


if __name__ == "__main__":
    print(getNthFib(1))
    print(getNthFib(2))
    print(getNthFib(6))