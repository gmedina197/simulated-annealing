import math
import random


class Senoidal:
    LOWER_INTERVAL = 0.0

    UPPER_INTERVAL = 4.0

    def __init__(self):
        self.population = []

    def get_value(self, x):
        return x * math.sin(10 * math.pi * x) + 5

    def generate_initial_population(self, size):
        for i in range(0, size):
            rand_num = random.uniform(self.LOWER_INTERVAL, self.UPPER_INTERVAL)
            self.population.append(rand_num)

    def print_atoms(self):
        print(self.population)

    def perturbate(self, index, lower_perturbation, upper_perturbation):
        self.candidate = self.population[index] + random.uniform(lower_perturbation, upper_perturbation)
        if (self.candidate > self.UPPER_INTERVAL):
            self.candidate = self.UPPER_INTERVAL
        elif (self.candidate < self.LOWER_INTERVAL):
            self.candidate = self.LOWER_INTERVAL
        return self.candidate

    def use_candidate(self, index):
        self.population[index] = self.candidate

    def get_maximum(self):
        max = self.population[0]
        index = 0
        for i, atom in enumerate(self.population):
            val = self.get_value(atom)
            if (val > max):
                max = val
                index = i
        return self.population[index], max


class Solver:
    def __init__(self, problem, repetitions, alpha, lower_bound, upper_bound, lower_perturbation, upper_perturbation):
        self.problem = problem
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.lower_perturbation = lower_perturbation
        self.upper_perturbation = upper_perturbation
        self.repetitions = repetitions
        self.alpha = alpha

    def maximize(self):
        t = self.upper_bound
        t_min = self.lower_bound
        while t > t_min:
            for i in range(1, self.repetitions):
                for index, atom in enumerate(self.problem.population):
                    candidate = self.problem.perturbate(index, self.lower_perturbation, self.upper_perturbation)
                    energy_delta = candidate - atom
                    if energy_delta >= 0:
                        self.problem.use_candidate(index)
                    else:
                        rnd = random.uniform(0.0, 1.0)
                        if (rnd < math.exp(energy_delta / t)):
                            self.problem.use_candidate(index)
            t = t * self.alpha


try:
    alpha = float(raw_input('Alpha [0.9]: '))
except ValueError:
    alpha = 0.9

try:
    repetitions = int(raw_input('Repetitions [10]: '))
except ValueError:
    repetitions = 10

try:
    atoms_count = int(raw_input('Atoms count [10]: '))
except ValueError:
    atoms_count = 10

try:
    lower_bound = float(raw_input('Lower bound [27]: '))
except ValueError:
    lower_bound = 27

try:
    upper_bound = float(raw_input('Upper bound [1538]:'))
except ValueError:
    upper_bound = 1538

try:
    lower_perturbation = float(raw_input('Lower perturbation [-1.0]: '))
except ValueError:
    lower_perturbation = -1.0

try:
    upper_perturbation = float(raw_input('Upper perturbation [1.0]: '))
except ValueError:
    upper_perturbation = 1.0

senoidal_problem = Senoidal()
senoidal_problem.generate_initial_population(atoms_count)

solver = Solver(senoidal_problem, repetitions, alpha, lower_bound, upper_bound, lower_perturbation, upper_perturbation)
solver.maximize()

x, y = senoidal_problem.get_maximum()

print("x: " + str(x))
print("y: " + str(y))
