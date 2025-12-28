def responses_creator_original(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    responses = []
    for item_id in item_ids:
        new_response = dict(item_id=item_id)  # Исправлена ошибка: было item_id-item_id
        responses.append(new_response)
    return responses


def responses_creator_optimized(item_ids):
    # Если item_ids is None, используем пустой список
    if item_ids is None:
        item_ids = []

    # List comprehension для создания списка словарей
    return [{'item_id': item_id} for item_id in item_ids]


# Функция f как в примере задания
def f(item_ids):
    return responses_creator_optimized(item_ids)


# Пример использования и тестирование
if __name__ == "__main__":
    print("=== Тестирование оптимизированного кода ===\n")

    # Тест 1: Нормальный список
    test1 = [1, 2, 3]
    result1 = f(test1)
    print(f"1. f({test1}) = {result1}")

    # Тест 2: Пустой список
    test2 = []
    result2 = f(test2)
    print(f"2. f({test2}) = {result2}")

    # Тест 3: None (особый случай)
    test3 = None
    result3 = f(test3)
    print(f"3. f({test3}) = {result3}")

    # Тест 4: Один элемент
    test4 = [42]
    result4 = f(test4)
    print(f"4. f({test4}) = {result4}")

    print("\n=== Сравнение с оригиналом ===")

    # Сравнение производительности (опционально)
    import time

    test_data = list(range(1000))

    # Оригинальная версия
    start = time.time()
    original_result = responses_creator_original(test_data)
    original_time = time.time() - start

    # Оптимизированная версия
    start = time.time()
    optimized_result = responses_creator_optimized(test_data)
    optimized_time = time.time() - start

    print(f"\nОригинальная версия: {original_time:.6f} сек")
    print(f"Оптимизированная версия: {optimized_time:.6f} сек")
    print(f"Ускорение: {original_time / optimized_time:.2f}x")

    # Проверка что результаты одинаковые
    assert original_result == optimized_result, "Результаты должны совпадать!"
    print("\n✓ Результаты обеих функций идентичны")