import itertools


def combine_lists(*lists):
    # Используем itertools.chain для объединения списков
    combined = itertools.chain(*lists)
    return list(combined)


def f(list1, list2):
    return combine_lists(list1, list2)


if __name__ == "__main__":
    result = f([1, 2], [3, 4])
    print(f"list(f([1, 2], [3, 4])) = {result}")

    print(f"\nДополнительные тесты:")

    test1 = combine_lists([1, 2], [3, 4], [5, 6])
    print(f"3 списка: {test1}")

    test2 = combine_lists([1, 2], [], [3, 4])
    print(f"С пустым списком: {test2}")

    test3 = combine_lists(['a', 'b'], ['c', 'd'])
    print(f"Строки: {test3}")