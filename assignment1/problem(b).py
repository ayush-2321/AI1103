
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random

#number of simulations
simlen=10000

#number of draws
n=5

#case 1: Finding probability of draw of all spades from a well shuffled deck of cards
# For simulating this we create a list of 52 integers and assume first 13 integers to be a spade. For each simulation we shuffle our list and choose first five elements in the list.

list_deck =(list)(range(1,53))

success=0
for i in range(10000):
    count_spade=0
    random.shuffle(list_deck)
    for j in range(0,5):
        if list_deck[j] >=1 and list_deck[j] <=13:
            count_spade +=1
        
    if count_spade ==5:
        success +=1

print("The simulated probability of all spades is",success/10000)

#case 2: Finding probability of draw of 3 spades from 5 draw from a well shuffled deck of cards
#using the same method as above

list_deck =(list)(range(1,53))

success=0
for i in range(10000):
    count_spade=0
    random.shuffle(list_deck)
    for j in range(0,5):
        if list_deck[j] >=1 and list_deck[j] <=13:
            count_spade +=1
        
    if count_spade ==3:
        success +=1
        
print("The simulated probability of 3 spades is",success/10000)

#case 3: Finding probability of draw of no spade

list_deck =(list)(range(1,53))

success=0
for i in range(10000):
    count_spade=0
    random.shuffle(list_deck)
    for j in range(0,5):
        if list_deck[j] >=1 and list_deck[j] <=13:
            count_spade +=1
        
    if count_spade ==0:
        success +=1
        
print("The simulated probability of no spades is",success/10000)