import random
from deap import base, creator, tools, algorithms

# Fitness: maximize
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox setup
toolbox = base.Toolbox()
toolbox.register("bit", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.bit, 5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Evaluation function: x^2
def eval(ind):
    x = int("".join(map(str, ind)), 2)
    return x * x,

toolbox.register("evaluate", eval)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run GA 
pop = toolbox.population(n=10)
algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, verbose=True)

# Show best solution
best = tools.selBest(pop, 1)[0]
x = int("".join(map(str, best)), 2)
print(f"\nBest: {best} -> x = {x}, x^2 = {x**2}")
