import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dimensions = len(bounds)
    current_solution = [random.uniform(*b) for b in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        # Генеруємо сусідню точку
        neighbor = [
            max(
                min(current_solution[i] + random.uniform(-0.1, 0.1), bounds[i][1]),
                bounds[i][0],
            )
            for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        # Оновлюємо, якщо знайшли краще значення
        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

        # Перевірка на epsilon
        if abs(neighbor_value - current_value) < epsilon:
            break

    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(*b) for b in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(*b) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
        func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    dimensions = len(bounds)
    current_solution = [random.uniform(*b) for b in bounds]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value

    for _ in range(iterations):
        # Генеруємо сусідню точку
        neighbor = [
            max(
                min(current_solution[i] + random.uniform(-0.1, 0.1), bounds[i][1]),
                bounds[i][0],
            )
            for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        # Приймаємо нову точку за правилом Метрополіса
        if neighbor_value < current_value or random.random() < math.exp(
                (current_value - neighbor_value) / temp
        ):
            current_solution, current_value = neighbor, neighbor_value

        # Оновлюємо найкраще рішення
        if current_value < best_value:
            best_solution, best_value = current_solution, current_value

        # Зменшуємо температуру
        temp *= cooling_rate

        if temp < epsilon:
            break

    return best_solution, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
