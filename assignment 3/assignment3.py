import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random



#number of simulations
simlen=100000

b1=('red','red','red','white','white','white')  #box b1 items
b2=('red','red','red','red','white','white')    #box b2 items
success=0

#now using the condition given in question we run the simulation. Note that we applied random choice twice instead of size 2 because its draw with replacement.

for i in range(simlen):
    die=random.randrange(1,7)
    if die%2==0 or die==5:
        color1=random.choice(b1)
        color2=random.choice(b1)
        
    else:
        color1=random.choice(b2)
        color2=random.choice(b2)
        
    if color1 != color2:
        success +=1
        
print("So, probability obtained after simulation is:",success/100000)
print("Theoritical probability is:",13/27)

