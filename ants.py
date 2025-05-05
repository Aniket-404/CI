import numpy as np
import random

NUM_CITIES = 5
NUM_ANTS = 5
ITERATIONS = 50
ALPHA = 1.0
BETA = 2.0
EVAPORATION = 0.5
Q = 100

distances = np.random.randint(10, 100, (NUM_CITIES, NUM_CITIES))
np.fill_diagonal(distances, 0)
pheromone = np.ones((NUM_CITIES, NUM_CITIES))

def select_next(city, visited):
    probs = [(pheromone[city][i]**ALPHA / distances[city][i]**BETA, i) for i in range(NUM_CITIES) if i not in visited]
    return max(probs)[1] if probs else visited[0]

def construct_path():
    path = [random.randint(0, NUM_CITIES - 1)]
    while len(path) < NUM_CITIES:
        path.append(select_next(path[-1], path))
    path.append(path[0])
    return path

def update_pheromone(paths):
    global pheromone
    pheromone *= (1 - EVAPORATION)
    for path in paths:
        length = sum(distances[path[i]][path[i + 1]] for i in range(NUM_CITIES))
        for i in range(NUM_CITIES):
            pheromone[path[i]][path[i + 1]] += Q / length

def main():
    for _ in range(ITERATIONS):
        paths = [construct_path() for _ in range(NUM_ANTS)]
        update_pheromone(paths)
    best_path = min(paths, key=lambda p: sum(distances[p[i]][p[i + 1]] for i in range(NUM_CITIES)))
    print("Best path:", best_path)

if __name__ == "__main__":
    main()
    