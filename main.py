def solve():
    n = int(input())
    
    # Исходное состояние
    in_city = True          # начинаем в населенном пункте
    on_highway = False      # не на автомагистрали
    limit = None            # текущее временное ограничение (None если нет)
    
    # Ограничения по умолчанию
    CITY_DEFAULT = 60
    NON_CITY_DEFAULT = 90
    HIGHWAY_DEFAULT = 110
    
    results = []
    
    for _ in range(n):
        event = input().strip().split()
        event_type = event[0]
        
        # Обрабатываем события
        if event_type == "city":
            # Начало населенного пункта
            in_city = True
            on_highway = False
            limit = None  # сбрасываем временное ограничение
            
        elif event_type == "nocity":
            # Конец населенного пункта
            in_city = False
            limit = None  # сбрасываем временное ограничение
            
        elif event_type == "highway":
            # Начало автомагистрали
            on_highway = True
            limit = None  # сбрасываем временное ограничение
            
        elif event_type == "nohighway":
            # Конец автомагистрали
            on_highway = False
            limit = None  # сбрасываем временное ограничение
            
        elif event_type == "limit":
            # Временное ограничение скорости
            limit = int(event[1])
            
        elif event_type == "nolimit":
            # Отмена временного ограничения
            limit = None
            
        elif event_type == "cross":
            # Перекресток
            limit = None  # сбрасываем временное ограничение
        
        # Определяем текущую максимальную скорость
        if limit is not None:
            # Если есть временное ограничение
            current_speed = limit
        else:
            # Используем ограничение по умолчанию
            if on_highway:
                current_speed = HIGHWAY_DEFAULT
            elif in_city:
                current_speed = CITY_DEFAULT
            else:
                current_speed = NON_CITY_DEFAULT
        
        results.append(str(current_speed))
    
    # Выводим результаты
    print("\n".join(results))

if __name__ == "__main__":
    solve()
