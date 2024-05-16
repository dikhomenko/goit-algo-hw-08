import heapq

def min_cost_to_connect_cables(cables):
    # Створення мін-купи з початкового списку кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Повторювати до тих пір, поки в купі більше одного елемента
    while len(cables) > 1:
        # Вилучити два найменших кабелі
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Об'єднати їх, обчислити витрати на з'єднання
        cost = first_min + second_min
        total_cost += cost
        
        # Додати отриманий кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
