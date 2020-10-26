# **Introduction**

There is a container which has **n** number of balls of **5** different colors - Orange , Green , Blue , Violet, Red.
Each of the color's balls are generated from Discrete Uniform Distribution, yielding approximately same number of balls of each color. We conduct hypothesis testing using Frequentist and Bayesian inference to check whether the propotion of Red ball is **0.2**.

# Imports and mapping
"""

import numpy as np 
from scipy.stats import binom
# map is dictionary with maps numbers to colors 
map={}
map[0]="Red";map[1]="Green";map[2]="Blue";map[3]="Violet";map[4]="Orange"
#Description - if the number is i, it means that the corresponding color is map[i]

"""# Data Generation"""

n = 500 # size of sample
# Generating data of size n from uniform distribution
data = np.random.randint(0,5,size=n)

"""# ***Frequentist*** Inference"""

'''
Frequentist inference
p = propotion of Red balls
Hypotheseses
H_0 : p = 0.2 
H_A : p > 0.2
Significance level- alpha = 0.05
'''
#Significance level(alpha/Type-1 Error)

alpha = 0.05

# p_0 = Value of p given H_0 is True

p_0 = 0.2

# Counting Total number of Red balls in a sample of size n

k = np.count_nonzero(data==0) 
print("Total number of Red balls in a sample of size",n,"is",k)

#Calculating p-value
'''
t~Binomial(n,p)
# p_value = P(t>=k|n=,p=0.2){Probability that random variable t is greater than equal to k, t~Binom(n,p)}
'''
p_value = 1 - binom.cdf(k-1,n,p_0)

if p_value>alpha:
  print("Unable to reject H_0 since p-value =",p_value,"which is greater than alpha.")
else:
  print("Reject H_0 since p-value =",p_value,"which is less than alpha.")

"""# ***Bayesian*** Inference"""

'''
Bayesian Approch
p = propotion of Red balls
H_1 : p = 0.25
H_2 : p = 0.2
'''
#Prior

p_H_1 = 0.5
p_H_2 = 0.5

#Hypotheses

p1 = 0.25
p2 = 0.2

# Counting Total number of Red balls in a sample of size n

k = np.count_nonzero(data==0) 
print("Total number of Red balls in a sample of size",n,"is",k)

#Computing likelihoods 

p_given_H_1 = binom.pmf(k, n, p1) #P(number of Red balls=k|H_1)
p_given_H_2 = binom.pmf(k, n, p2) #P(number of Red balls=k|H_2)
print("P(number of Red balls=k|H_1) : ",p_given_H_1)
print("P(number of Red balls=k|H_2) : ",p_given_H_2)
p_total = p_given_H_1*p_H_1 + p_given_H_2*p_H_2

#Posterior

p_H_1_post = (p_given_H_1*p_H_1)/p_total #P(H_1|number of Red balls=k)
p_H_2_post = (p_given_H_2*p_H_2)/p_total #P(H_2|number of Red balls=k)
print("P(H_1|number of Red balls=k) : ",p_H_1_post)
print("P(H_2|number of Red balls=k) : ",p_H_2_post)

#Selecting the most probable Hypotheses
if (p_H_1_post > p_H_2_post):
  print("Since P(H_1|number of Red balls=k) > P(H_2|number of Red balls=k), we would pick H_1 which has posterior of",p_H_1_post)
else:
  print("Since P(H_2|number of Red balls=k) > P(H_1|number of Red balls=k), we would pick H_2 which has posterior of",p_H_2_post)

L = [10,30,50,100,300,500,1000]
p_0 = 0.2
p1 = 0.25
p2 = 0.2
for n in L:
  print("for n=",n)
  data = np.random.randint(0,5,size=n)
  k = np.count_nonzero(data==0) 
  print("Total number of Red balls in a sample of size",n,"is",k)
  p_value = 1 - binom.cdf(k-1,n,p_0)
  if p_value>alpha:
    print("Unable to reject H_0 since p-value =",p_value,"which is greater than alpha.")
  else:
    print("Reject H_0 since p-value =",p_value,"which is less than alpha.")
  p_given_H_1 = binom.pmf(k, n, p1) #P(number of Red balls=k|H_1)
  p_given_H_2 = binom.pmf(k, n, p2) #P(number of Red balls=k|H_2)
  p_total = p_given_H_1*p_H_1 + p_given_H_2*p_H_2
  p_H_1_post = (p_given_H_1*p_H_1)/p_total #P(H_1|number of Red balls=k)
  p_H_2_post = (p_given_H_2*p_H_2)/p_total #P(H_2|number of Red balls=k)
  print("P(H_1|number of Red balls=k) : ",p_H_1_post)
  print("P(H_2|number of Red balls=k) : ",p_H_2_post)
  if (p_H_1_post > p_H_2_post):
    print("Since P(H_1|number of Red balls=k) > P(H_2|number of Red balls=k), we would pick H_1 which has posterior of",p_H_1_post)
  else:
    print("Since P(H_2|number of Red balls=k) > P(H_1|number of Red balls=k), we would pick H_2 which has posterior of",p_H_2_post)
