import random

class Senoidal:
    LOWER_INTERVAL = 0.0

    UPPER_INTERVAL = 4.0

    def __init__(self):
        self.population = []

    def generate_initial_population(self, size):
        for i in range(0, int(size)):
            rand_num = random.uniform(self.LOWER_INTERVAL, self.UPPER_INTERVAL)
            self.population.append(rand_num)

    def print_population(self):
        for item in self.population:
            print(str(item))

alpha = input('Alpha: ')
repetitions = input('Repetitions: ')
pop_size = input('Population size: ')
lower_bound = input('Lower bound: ')
upper_bound = input('Upper bound: ')

senoidal_problem = Senoidal()
senoidal_problem.generate_initial_population(pop_size)
senoidal_problem.print_population()