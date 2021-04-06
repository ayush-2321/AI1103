import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random



#number of simulations
simlen=100000


success=0

#we run a simulation for sample size 100000 and take 2 random nos between 1 to 6 (inclusive) 

for i in range(simlen):
    die_sample=random.sample(range(1,7),2)
    sum=die_sample[0]+ die_sample[1]
    if sum==8:
        success +=1
        
print("So, probability obtained after simulation is:",success/100000)
print("Theoritical probability is:",5/36)
