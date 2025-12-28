import random


def generate_fractions(n):
    for _ in range(n):
        yield random.uniform(0, n)


def f(n):
    return generate_fractions(n)


if __name__ == "__main__":
    result = list(f(3))
    print(f"list(f(3)) = {result}")

    print(f"\nДополнительные тесты:")
    print(f"5 чисел в [0, 5]: {list(f(5))}")
    print(f"1 число в [0, 1]: {list(f(1))}")