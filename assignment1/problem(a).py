import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom




#Simlen
simlen=1000

#Number of questions
n =  5

#Probability of  solving a question
p = 1/3

#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of solving 5 question

count=0

for i in range(1000):
    if data_binom[i]>=4:
        count +=1

print("probability of solving 4 or more question just by guessing using simulation is",count/1000)
print("Theoritical probability of solving 4 or more quetion just by guessing is",11/243)      