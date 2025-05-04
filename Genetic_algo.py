import random
import numpy as np
from deap import base, creator, tools, algorithms

#create the fitness function and individual class
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Define the evaluation function
def eval_nn(ind):
    return np.random.rand(),

# Initialize the toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0.1, 1.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_nn)

# Main GA loop
def main():
    pop = toolbox.population(n=10)
    ngen = 10
    cxpb = 0.5
    mutpb = 0.2
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    algorithms.eaSimple(pop, toolbox, cxpb, mutpb, ngen, stats=stats, verbose=True)
    print("Best parameters: ", tools.selBest(pop, 1)[0])

if __name__ == "__main__":
    main()
