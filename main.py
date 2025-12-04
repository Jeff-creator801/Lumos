def solve():
    n = int(input())
    m = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    # Пассажиры: A*i + B, i = 0..n-1
    # Таксисты: C*j + D, j = 0..m-1
    
    # P(X) = количество пассажиров с A*i + B >= X
    # P(X) = n - ceil(max(0, X - B)/A) если X > B, иначе n
    # T(X) = количество таксистов с C*j + D <= X
    # T(X) = min(m, floor((X - D)/C) + 1) если X >= D, иначе 0
    
    def P(X):
        if X > A*(n-1) + B:
            return 0
        if X <= B:
            return n
        # X > B
        # i >= (X - B) / A
        min_i = (X - B + A - 1) // A  # ceil
        if min_i < 0:
            return n
        return max(0, n - min_i)
    
    def T(X):
        if X < D:
            return 0
        # j <= (X - D) / C
        max_j = (X - D) // C
        if max_j < 0:
            return 0
        return min(m, max_j + 1)
    
    # Бинарный поиск X, где P(X) >= T(X) и P(X+1) < T(X+1) ? 
    # Но проще: перебираем X среди "критических" точек:
    # Критические для P: X = A*i + B + 1 (граница, где пассажир i перестает платить)
    # Критические для T: X = C*j + D (граница, где таксист j начинает работать)
    
    candidates = set()
    # Границы для X
    low = D
    high = A*(n-1) + B
    
    # Критические точки:
    for i in range(n):
        candidates.add(max(D, A*i + B))       # максимальная цена для пассажира i
        candidates.add(min(high, A*i + B + 1)) # на 1 больше — он уже не может
    for j in range(m):
        candidates.add(max(D, C*j + D))       # минимальная цена для таксиста j
        candidates.add(min(high, C*j + D + 1)) # на 1 больше — ещё может
    
    # Добавляем low и high
    candidates.add(low)
    candidates.add(high)
    
    # Удалим слишком большие/маленькие
    candidates = [x for x in candidates if D <= x <= high]
    
    # Ищем оптимальный
    best_match = -1
    best_X = -1
    
    for X in candidates:
        matches = min(P(X), T(X))
        if matches > best_match or (matches == best_match and X > best_X):
            best_match = matches
            best_X = X
    
    # Проверим X-1 и X+1 для safety
    for dx in [-1, 1]:
        X = best_X + dx
        if X < D or X > high:
            continue
        matches = min(P(X), T(X))
        if matches > best_match or (matches == best_match and X > best_X):
            best_match = matches
            best_X = X
    
    print(best_X)

if __name__ == "__main__":
    solve()
