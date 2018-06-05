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

    def print_population(self):
        for item in self.population:
            print(str(item))


class Solver:
    def __init__(self, problem, lower_bound, upper_bound):
        self.problem = problem
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def perturbate_current(self):
        pass

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
    pop_size = int(raw_input('Population size [10]: '))
except ValueError:
    pop_size = 10

try:
    lower_bound = float(raw_input('Lower bound [27]: '))
except ValueError:
    lower_bound = 27

try:
    upper_bound = float(raw_input('Upper bound [1538]:'))
except ValueError:
    upper_bound = 1538

senoidal_problem = Senoidal()
senoidal_problem.generate_initial_population(pop_size)
senoidal_problem.print_population()
