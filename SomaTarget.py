
# Objetivo: algoritmo genético para o problema da mochila . Tentar chegar o mais próximo do target.

#O algoritmo rodara epochs vezes -> numero de populacoes geradas. Sera impresso a media de fitness de cada uma das epochs populacoes


  
from genetic2020 import *
from Mochila import mochila_main

itens = [[2,12],[1,10],[3,20],[2,15]] # item com o seu peso e valor [peso,valor]
peso = 5 #kg
target = mochila_main(itens,peso) # número alvo (melhor solução para esse conjunto de itens)
i_length = len(itens) #posições do vetor
i_min = 0 #range mínimo (item não contido)
i_max = 1 #range máximo (item não contido)
p_count = 20 #individuos por geração
epochs = 20 #épocas, quantas gerações eu vou gerar
p = population(p_count, i_length, i_min, i_max) #criando a minha população
fitness_history = [media_fitness(p, itens, peso),] #histórico de confiabilidade de cada indivíduo

for i in range(epochs): #processando as épocas
    p = evolve(p, itens, peso, target)
    fitness_history.append(media_fitness(p, itens, peso))


for datum in fitness_history: #printando todos os fitness médios
   print (datum)

print("Objetivo: {}".format(target))
