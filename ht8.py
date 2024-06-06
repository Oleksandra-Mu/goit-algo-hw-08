import heapq
import numpy as np

def min_cost(cable_lengths):
    # загальні витрати
    total_cost = 0
    heapq.heapify(cable_lengths)


    # поєднання кабелів
    while len(cable_lengths) > 1:
        # отримуємо два найменших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # поєднання кабелів 
        combined = first + second
        total_cost += combined

        # додаємо поєднаний кабель до купи
        heapq.heappush(cable_lengths, combined)

    return total_cost

# Приклади використання функції
cable_lengths = list(np.random.randint(low=0, high=20, size=(6)))
print(cable_lengths)
print(f"Мінімальні загальні витрати: {min_cost(cable_lengths)}")