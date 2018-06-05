import math
import random


class Problem:

    def __init__(self):
        self.population = []
        self.best_atom = None
        self.best_f = None

    def print_atoms(self):
        print(self.population)

    def getLowerInterval(self):
        pass

    def getUpperInterval(self):
        pass

    def get_value(self, atom):
        pass

    def perturbate(self, index, lower_perturbation, upper_perturbation):
        self.candidate = dict()
        upper_interval = self.getUpperInterval()
        lower_interval = self.getLowerInterval()
        atom = self.population[index]
        for key in atom:
            self.candidate[key] = atom[key] + random.uniform(lower_perturbation, upper_perturbation)
            if (self.candidate[key] > upper_interval[key]):
                self.candidate[key] = upper_interval[key]
            elif (self.candidate[key] < lower_interval[key]):
                self.candidate[key] = lower_interval[key]
        return self.candidate

    def use_candidate(self, index):
        self.population[index] = self.candidate

    def update_best(self):
        for i, atom in enumerate(self.population):
            val = self.get_value(atom)
            if (val > self.best_f):
                self.best_atom = self.population[i]
                self.best_f = val

    def get_best(self):
        return self.best_atom, self.best_f


class Senoidal(Problem):

    def getLowerInterval(self):
        return {'x': 0.0}

    def getUpperInterval(self):
        return {'x': 4.0}

    def get_value(self, atom):
        return atom['x'] * math.sin(10 * math.pi * atom['x']) + 5

    def generate_initial_population(self, size):
        for i in range(0, size):
            lower = self.getLowerInterval()
            upper = self.getUpperInterval()
            rand_num = random.uniform(lower['x'], upper['x'])
            self.population.append({'x': rand_num})


class QuadriGaussian(Problem):

    def getLowerInterval(self):
        return {'x': -5.0, 'y': -5.0}

    def getUpperInterval(self):
        return {'x': 5.0, 'y': 5.0}

    def get_value(self, atom):
        a = 0.97 * math.exp(- (math.pow(atom['x'] + 3, 2) + math.pow(atom['y'] + 3, 2)) / 5)
        b = 0.98 * math.exp(- (math.pow(atom['x'] + 3, 2) + math.pow(atom['y'] - 3, 2)) / 5)
        c = 0.99 * math.exp(- (math.pow(atom['x'] - 3, 2) + math.pow(atom['y'] + 3, 2)) / 5)
        d = 1.00 * math.exp(- (math.pow(atom['x'] - 3, 2) + math.pow(atom['y'] - 3, 2)) / 5)
        return a + b + c + d

    def generate_initial_population(self, size):
        lower = self.getLowerInterval()
        upper = self.getUpperInterval()
        for i in range(0, size):
            new_atom = dict()
            rand_num = random.uniform(lower['x'], upper['x'])
            new_atom['x'] = rand_num
            rand_num = random.uniform(lower['y'], upper['y'])
            new_atom['y'] = rand_num
            self.population.append(new_atom)


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
                    energy_delta = self.problem.get_value(candidate) - self.problem.get_value(atom)
                    if energy_delta >= 0:
                        self.problem.use_candidate(index)
                    else:
                        rnd = random.uniform(0.0, 1.0)
                        if (rnd < math.exp(energy_delta / t)):
                            self.problem.use_candidate(index)
                self.problem.update_best()
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
    lower_bound = float(raw_input('Lower bound [0.1]: '))
except ValueError:
    lower_bound = 0.1

try:
    upper_bound = float(raw_input('Upper bound [100]:'))
except ValueError:
    upper_bound = 100

try:
    lower_perturbation = float(raw_input('Lower perturbation [-1.0]: '))
except ValueError:
    lower_perturbation = -1.0

try:
    upper_perturbation = float(raw_input('Upper perturbation [1.0]: '))
except ValueError:
    upper_perturbation = 1.0

# Senoidal

senoidal_problem = Senoidal()
senoidal_problem.generate_initial_population(atoms_count)

solver = Solver(senoidal_problem, repetitions, alpha, lower_bound, upper_bound, lower_perturbation, upper_perturbation)
solver.maximize()

atom, f = senoidal_problem.get_best()

print(atom)
print("f(x): " + str(f))

# QuadriGaussian

quadri_gaussian = QuadriGaussian()
quadri_gaussian.generate_initial_population(atoms_count)

solver = Solver(quadri_gaussian, repetitions, alpha, lower_bound, upper_bound, lower_perturbation, upper_perturbation)
solver.maximize()

atom, f = quadri_gaussian.get_best()

print(atom)
print("f(x, y): " + str(f))