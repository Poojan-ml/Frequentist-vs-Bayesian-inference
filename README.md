# Frequentist-vs-Bayesian-inference
This is an experiment to learn and understand the differnce between Frequentist and Bayesian Inference. The code is well commented and self-explanatory. 
We simulate an experiment and conduct hypothesis testing using Frequentist and Bayesian inference. We generate a sample with n balls of 5 different colors - Red , Green , Blue , Violet, Orange. Each of the ball’s color is picked from Discrete Uniform Distribution over the 5 colors, yielding approximately the same number of balls of each color. We conduct hypothesis testing using Frequentist and Bayesian inference to check whether the proportion of Red balls is 0.2.
Let p be the proportion of Red balls in the sample. 
Frequentist Inference
Hypothesis
H0 : p = 0.2 
HA : p > 0.2
Significance level- α = 0.05
We observe ‘k’ number of Red balls in the sample and calculate the p-value.
Let a random variable T represent  the number of Red balls.
The random variable T follows a binomial distribution with parameters n,p0. (T~Binom(n,p0))
And let F(T) be the cumulative mass function for the random variable T. 
p-value = P(T ≥  k) = 1 - P(T<k) = 1 - F(k-1)
If p-value>α ,we fail to reject the null hypothesis else we reject the null hypothesis. 
 
Bayesian Inference
Hypothesis 
H1 : p =  0.25       
H2  : p = 0.2
Prior
There is no reason to be biased towards any of the hypotheses initially.
P(H1) = 0.5
P(H2) = 0.5 
Again we observe k Red balls. 
We calculate the likelihood of the same for each of the hypotheses.
Once again let a random variable T represent  the number of Red balls.
The random variable T follows a binomial distribution with parameters n,p. (T~Binom(n,p))
And let f1(T) and f2(T) be the probability mass functions for the random variable T with parameters (n, p1) and (n,p2) respectively. 
P(T = k|H1) = f1(k)
P(T = k|H2) = f2(k)
And the total probability P(T = k) = P(H1)*P(T = k|H1) + P(H2)*P(T = k|H2)
Now we calculate the posterior for each hypothesis. 
P(H1|T = k) = P(H1)*P(T = k|H1)/P(T = k)
P(H2|T = k) = P(H2)*P(T = k|H2)/P(T = k)
And we would pick hypotheses which have higher posterior. 
We repeat this experiment for different sample sizes and here is a summary of results. 
Here on last 2 columns green sign means that we would choose corresponding Hypothesis
 


