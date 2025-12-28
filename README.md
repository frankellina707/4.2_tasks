## Задание 1: Генератор случайных дробных чисел
**Папка:** `4_2_TASK1`
### Файлы:
- `random_generator.py` - основной код
### Запуск:
```bash
cd task1_random
python random_generator.py
```
## Задание 2: Генератор случайных дробных чисел
**Папка:** `4_2_TASK2`
### Файлы:
- `list_chain.py` - основной код
### Запуск:
```bash
cd 4_2_TASK2
python list_chain.py
```

## Задание 3: Оптимизация кода
**Папка:** `4_2_TASK3/`

### Что было исправлено:
1. Исправлена ошибка: `dict(item_id-item_id)` → `dict(item_id=item_id)`
2. Улучшена обработка None (теперь возвращает `[]` вместо `[None]`)
3. Заменен цикл for на list comprehension
4. Убраны ненужные временные переменные

### Файлы:
- `optimize_code.py` - основной код с обеими версиями функций

### Запуск:
```bash
cd 4_2_TASK3
python optimize_code.py