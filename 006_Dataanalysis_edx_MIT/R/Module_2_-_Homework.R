rm(list = ls())
library(dplyr)
library(ggplot2)

#rbinom(n, size, prob)
#where n refers to number of observations, size refers to number of trials, 
#and prob refers to probability of success on each trial

n <- 8
p <- 0.2

successes <- rbinom(10000,n,p)

#Question 9&10
hist(successes)

#Question 12
#probability of getting exactly 7 heads on 10 flips
#dbinom(x, size, prob) where x is the observations, 
#size is number of trials, prob is probability
#pbinom(q, size, prob) where q is the number of observations,
#size is the number of trials, prob is the probability

#Part A
dbinom(7,10,0.65)
#Part B
1-dbinom(8,10,0.65)-dbinom(9,10,0.65)-dbinom(10,10,0.65)
pbinom(7,10,0.65)
#Part C
dbinom(6,10,0.65)+dbinom(7,10,0.65)+dbinom(8,10,0.65)+dbinom(9,10,0.65)+dbinom(10,10,0.65)
1-pbinom(5,10,0.65)

#Question 14
binom_draws <- as_tibble(data.frame(successes))

estimated_pf <- binom_draws %>%
  group_by(successes) %>%
  summarize(n=n()) %>%
  mutate(freq=n/sum(n))

ggplot(estimated_pf, aes(x=successes, y=freq)) +
  geom_col() +
  ylab("Estimated Density")

#Question 15
#Create a tibble with x and the analytical probability densities.
my_binom<-as_tibble(list(x=0:n, prob=dbinom(0:n, n, p)))

#Plot the computed theoretical density.
ggplot(my_binom, aes(x=x, y=prob)) + geom_col() +
  ylab("Analytical Density")

calculated_cdf <- my_binom %>%
  mutate(cdf=cumsum(prob))

#Plot the computed cdf
ggplot(calculated_cdf, aes(x=x, y=cdf)) + geom_step() + 
  ylab("CDF")