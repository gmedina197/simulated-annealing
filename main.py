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

    def perturbate(self, lower_perturbation, upper_perturbation):
        for i, atom in enumerate(self.population):
            self.population[i] = atom + random.uniform(lower_perturbation, upper_perturbation)


class Solver:
    def __init__(self, problem, lower_bound, upper_bound, lower_perturbation, upper_perturbation):
        self.problem = problem
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.lower_perturbation = lower_perturbation
        self.upper_perturbation = upper_perturbation

    def perturbate_current(self):
        self.problem.perturbate(self.lower_perturbation, self.upper_perturbation)

    def run(self):
        self.perturbate_current()


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

solver = Solver(senoidal_problem, lower_bound, upper_bound, lower_perturbation, upper_perturbation)
solver.run()