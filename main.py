n = int(input())

# Считываем объекты и сохраняем их порядок
objects = []
for _ in range(n):
    obj = input().strip()
    objects.append(obj)

# Создаем словарь для быстрого поиска индекса объекта
index_map = {obj: i for i, obj in enumerate(objects)}

q = int(input())

results = []

# Обрабатываем запросы
for _ in range(q):
    query = input().strip()
    idx = index_map[query]
    
    # Создаем one-hot вектор
    vector = ['0'] * n
    vector[idx] = '1'
    
    results.append(' '.join(vector))

# Выводим результаты
for result in results:
    print(result)
