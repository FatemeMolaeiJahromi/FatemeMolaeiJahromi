#Fateme Molaei Jahromi
#40216341070006

import numpy as np

class ABC:
    def __init__(self, func, lower_bound, upper_bound, dimension, num_bees, max_iter):
        self.func = func
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimension = dimension
        self.num_bees = num_bees
        self.max_iter = max_iter
        self.food_sources = np.random.uniform(lower_bound, upper_bound, (num_bees, dimension))
        self.fitness = np.apply_along_axis(self.func, 1, self.food_sources)
        self.trial = np.zeros(num_bees)
    
    def employed_bees_phase(self):
        for i in range(self.num_bees):
            k = i
            while k == i:
                k = np.random.randint(0, self.num_bees)
            phi = np.random.uniform(-1, 1, self.dimension)
            new_solution = self.food_sources[i] + phi * (self.food_sources[i] - self.food_sources[k])
            new_solution = np.clip(new_solution, self.lower_bound, self.upper_bound)
            new_fitness = self.func(new_solution)
            if new_fitness < self.fitness[i]:
                self.food_sources[i] = new_solution
                self.fitness[i] = new_fitness
                self.trial[i] = 0
            else:
                self.trial[i] += 1
    
    def onlooker_bees_phase(self):
        fitness_prob = self.fitness / np.sum(self.fitness)
        for i in range(self.num_bees):
            if np.random.rand() < fitness_prob[i]:
                k = i
                while k == i:
                    k = np.random.randint(0, self.num_bees)
                phi = np.random.uniform(-1, 1, self.dimension)
                new_solution = self.food_sources[i] + phi * (self.food_sources[i] - self.food_sources[k])
                new_solution = np.clip(new_solution, self.lower_bound, self.upper_bound)
                new_fitness = self.func(new_solution)
                if new_fitness < self.fitness[i]:
                    self.food_sources[i] = new_solution
                    self.fitness[i] = new_fitness
                    self.trial[i] = 0
                else:
                    self.trial[i] += 1
    
    def scout_bees_phase(self):
        for i in range(self.num_bees):
            if self.trial[i] > self.max_iter / 2:
                self.food_sources[i] = np.random.uniform(self.lower_bound, self.upper_bound, self.dimension)
                self.fitness[i] = self.func(self.food_sources[i])
                self.trial[i] = 0
    
    def optimize(self):
        for _ in range(self.max_iter):
            self.employed_bees_phase()
            self.onlooker_bees_phase()
            self.scout_bees_phase()
        best_index = np.argmin(self.fitness)
        return self.food_sources[best_index], self.fitness[best_index]

# Example usage:
def sphere_function(x):
    return np.sum(x**2)

abc = ABC(func=sphere_function, lower_bound=-5, upper_bound=5, dimension=30, num_bees=50, max_iter=100)
best_solution, best_fitness = abc.optimize()
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
