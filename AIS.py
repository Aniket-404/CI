import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Triangular membership function
def triangular_membership(x, a=0.5, b=0.8, c=1.0):
    return max(0, min((x - a) / (b - a), (c - x) / (c - b)))

# AIS Class with training progress display
class AIS:
    def __init__(self, population_size=10, generations=10):
        self.population_size = population_size
        self.generations = generations

    def train(self, X_train, y_train):
        population = [RandomForestClassifier().fit(X_train, y_train) for _ in range(self.population_size)]

        for gen in range(1, self.generations + 1):
            print(f"\nGeneration {gen}/{self.generations}")

            # Fitness scores
            fitness_scores = [accuracy_score(y_train, clf.predict(X_train)) for clf in population]
            print("  Fitness scores:", np.round(fitness_scores, 3).tolist())

            # Membership values
            membership_values = [triangular_membership(f) for f in fitness_scores]
            print("  Membership values:", np.round(membership_values, 3).tolist())

            # Select top half
            best_indices = np.argsort(membership_values)[-self.population_size // 2:]
            print("  Selected indices:", best_indices.tolist())

            # Reproduce selected classifiers
            population = [population[i] for i in best_indices]
            while len(population) < self.population_size:
                population.append(RandomForestClassifier().fit(X_train, y_train))

        return population[0]

# Example with dummy structural data 
X, y = np.random.rand(100, 10), np.random.randint(0, 2, 100)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train using AIS
ais = AIS()
best_model = ais.train(X_train, y_train)

# Evaluate
y_pred = best_model.predict(X_test)
print(f"\nFinal Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
