# -*- coding: utf-8 -*-
"""GeneticAlgo_NQueens.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F-ZM2Q-qTjVuzH9H-Q0sMs7zeB9IVKyI
"""

import numpy
import random 
import matplotlib.pyplot as plt

random.seed(10)
numpy.random.seed(42)

MUTATION_RATE = 0.7

def fitness (cols):
    
    #horizontal collisions 
    
    hor_count = 0
    for i in range(len(cols)):
      for j in range( i+1, len(cols) ):
        if cols[i] == cols[j]:
          hor_count+=1
         # print(hor_count)

    #diagonal count 
    dia_count = 0
    for i in range(len(cols)):
      for j in range( i+1, len(cols) ):
        if (j - i) == (cols[j]-cols[i]):
          dia_count +=1
         # print(dia_count)

    return 1 + 28 - hor_count - dia_count


def crossover( state1, state2 ):
  crossover_point = random.randint(1,6)

  leftpart = numpy.array(state1[0:crossover_point])
  rightpart = numpy.array(state2[crossover_point:8])
  child = numpy.concatenate((leftpart,rightpart))
  return child 

def crossover_prob ( population ):
  weights = []
  total_fitness = 0
  for i in range(len(population)):
    total_fitness += fitness(population[i])
  for i in range(len(population)):
    weights.append(fitness(population[i])/ 29 ) 
  parents = random.choices( population, weights ,k =  2 )
  return parents 


def mutate( cols ):
  probability = random.random()
  if probability > MUTATION_RATE:
    index = random.randint(0,7)
    cols[index] = random.randint(0,7)

  return cols

# initial population 

def main():
  MUTATION_RATE = 0.8
  prob = []
  x = []
  y = []  

  population = []

  for i in range (20):
    r = 1
    population.append(numpy.array([r,r,r,r,r,r,r,r]))
  
  max_iter = 5000
  gen_best = -1
  best_fitness = 0

  for i in range (max_iter):
    new_population = []
    x.append(i)
    gen_best = -1
    MUTATION_RATE -= 0.01
    for j in range (len(population)):
      # parent1_index = random.randint(0, len(population)-1 )
      # parent2_index = random.randint(0, len(population)-1 )
      new_child = []

      crossover 
    # new_child = crossover( population[parent1_index], population[parent2_index] )

      parents = crossover_prob(population)
      new_child = crossover( parents[0], parents[1] )

      #mutate
    #mutated_new_child = []
      mutated_new_child = mutate(new_child)
      new_population.append(mutated_new_child)
      fit = fitness(mutated_new_child)
    
      print(fit)
    
      best_fitness = max( best_fitness, fit )
    
      if fit > gen_best: gen_best = fit
      
    
    population = new_population
    y.append(gen_best)
    if fit == 29: break


 
  
   

  print(best_fitness)
  
  plt.plot(x,y)
  plt.show

obj = main()

