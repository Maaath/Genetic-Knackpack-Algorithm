import random

def fitness_calc(individuals,itens,target):
    aux = []
    soma = 0
    for i in range(0,len(individuals)):
        for j in range(0,len(individuals[i])):
            soma += individuals[i][j] * itens[j][1]
        if soma > target: #fazemos o controle das soluções que são maiores que o nosso target,ou seja,inválidas
            soma = 0
        aux.append(soma)
        soma = 0

    return aux #fitness de todos os individuos de uma pop

def fitness_relative(fitness):
    soma=0
    aux=[]
    for x in fitness:
        soma+=x

    for y in fitness:
        if soma == 0:
            aux.append(0)
        else:
            aux.append(y/soma)
    return aux # fitness relativo de uma pop


def roleta_main(sort,pop):
    best_index = 0
    aux=[]
    best = pop[-1] + 1
    for i in range(0,len(pop)):
        if abs(pop[i]-sort) < best:
            best_index = pop[i]
            best = abs(pop[i]-sort)
    aux.append(best_index)
    pop.remove(best_index)
    return aux # faz a "roleta" e escolhe um individuo
    # (quanto > o seu fitness > a sua chance de ir para a próxima geração)


def roleta_start(individuals, itens, target, retain):
    fitness = fitness_calc(individuals, itens, target)
    fitness_rel = fitness_relative(fitness)
    pop = fitness_rel.copy()
    sort = random.uniform(0, 1) #sorteamos o valor aleatório para poder "girar" a roleta
    retain_length = int(len(fitness_rel) * retain) #calculamos quantos indivíduos serão selecionados
    if retain_length < 1: #garantimos que ao menos um indivíduo será selecionado
        retain_length = 1
    aux=[]
    for i in range(0, retain_length):
        roleta = roleta_main(sort,pop)
        aux.append(individuals[fitness_rel.index(roleta[0])])

    return aux #retorna os individuos selecionados pela roleta






