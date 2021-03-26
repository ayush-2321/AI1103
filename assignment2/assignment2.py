import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random



simlen=100000 #number of simulations

b=7 #number of boys

g=5 #number of girls

#For the purpose of simulation we create a list of girls and boys after which we randomly select 3 students from the list considering the weight.

students=["girl","boy"]




count=0  # number of girls in the selected students
success=0
for i in range(100000):
    count=0
    x=random.choices(students,weights=[g,b],k=3) #randomly selecting 3 students
    for j in range(0,3):
        if x[j]=="girl":
            count +=1
         
        
    if count >1:
        success +=1


print("Probability calculated by simulation is ",success/100000)    
print("Theoritical probability is",4/11)