

from random import randint, random
from operator import add
from functools import reduce
from Roleta import roleta_start


def individual(length, min, max):
    'Create a member of the population.' #vetor de len(itens) posições
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
    """
    Create a number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """ # p_count vetores de i_lenght posições
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual,itens,peso):
    fitness_calc = 0
    fitness_peso = 0
    for i in range(0,len(individual)):
        fitness_calc += individual[i] * itens[i][1] #fitness de um individuo
        fitness_peso += individual[i] * itens[i][0] #peso dessa solução

    if fitness_peso > peso: #indicamos que essa solução é inválida pois ultrapassa o limite de peso
        return fitness_calc * -1
    else:
        return fitness_calc #retornamos o fitness caso seja menor que o limite de peso

def media_fitness(pop, itens, peso):
    'Find average fitness for a population.'
    aux = []
    for i in range(0, len(pop)):
        soma = fitness(pop[i], itens, peso) #escalar
        aux.append(soma)

    summed = reduce(add, (abs(x) for x in aux))

    return summed / (len(pop) * 1.0) #média dos fitness dessa pop

def evolve(pop, itens, peso, target, retain=0.2, random_select=0.05, mutate=0.01):
    retain_length = int(len(pop)*retain)
    parents = roleta_start(pop,itens,target,retain)

    # randomicamente adiciona outros poucos indivíduos para promover diversidade genética
    for individual in pop[retain_length:]:
        if random_select > random():
            parents.append(individual)

    # faz mutação(crossover) em outros poucos indivíduos
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))

    # crossover parents to create children
    parents_length = len(parents)

    #descobre quantos filhos terao que ser gerados alem da roleta e aleatorios
    desired_length = len(pop) - parents_length
    children = []

    #comeca a gerar filhos que faltam
    while len(children) < desired_length:
        'escolhe pai e mae no conjunto de pais'
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            'gera filho metade de cada'
            child = male[:half] + female[half:]
            'adiciona novo filho a lista de filhos'
            children.append(child)
    'adiciona a lista de pais (roleta) os filhos gerados'
    parents.extend(children)
    return parents
