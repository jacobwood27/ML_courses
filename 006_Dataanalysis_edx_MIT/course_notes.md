---
title: Data Analysis for Social Scientists
toc: true
---

Instructors: Esther Duflo, Sara Fisher Ellison
Platform: edX  
Part of: Course 3/4 in the MITx Micromaster Program in Statistics and Data Science  
Started on: February 8, 2020  
Course link: [https://courses.edx.org/courses/course-v1:MITx+14.310x+1T2020/course/](https://courses.edx.org/courses/course-v1:MITx+14.310x+1T2020/course/)  


## Module 1: Introduction to the Course
- Data is beautiful
	- Social network viz example
- Data is insightful
	- Subsidized heating + pollution in China example
- Data is powerful
	- Auditing system imposed in pollution control India example
- Data can be deceitful
	- Organic food v autism example
	- Education v GDP example
- Correlation vs Causation

## Module 2: Fundamentals of Probability, Random Variables, Joint Distributions + Collecting Data
- Fundamentals of Probability
	- Sample space - collection of all possible outcomes
	- Event - thing that can happen
	- "c" - notation for contained in a set
	- "U" - notation for union (or)
	- $\cap$ - notation for intersection (and), but we leave this out in set theory
	- Mutually exclusive - similar to disjoint, no common outcome
	- Exhaustive - Spans the sample space
	- Simple sample space - events are countable and equally likely
	- Permutation - ordered arrangement of objects
		- Number of permutations of N objects = N!
		- Number of permutations of N choose n = N!/(N-n)!
	- Combination - unordered arrangement of objects
		- Number of combinations of N objects = N
		- Number of combinations of N choose n = N!/((N-n)! n!)
	- Independence - A and B are independent if the P of their intersection = product of their P
	- Conditional probability - Probability of A given B
		- P(A|B) = P(AB)/P(B)
	- Bayes' theorem
		- P(A|B) = P(B|A)P(A) / (P(B|A)P(A) + P(B|Ac)P(Ac))
	- Pick k from n with replacement
		- n^k
	- Pick k from n without replacement
		- n! / (n-k)!
- Random Variables
	- Discrete random variables - can be 
	- Continuous random variables - picked from an interval
		- Often discrete random variables can be modeled as continuous random variables
	- Hypergeometric distribution - number of successes in n trials when you're sampling without replacement from a sample size N whose initial probability of success was k/N
		- pizza with meat toppings and veggie toppings example
	- Binomial distribution - number of successes in n trials where the trials are independent and the probability of success in each is p
	- Probability function - Discrete random variable - f(x) = P(X=x)
	- Probability density function - Continuous random variable
	- Cumulative distribution function - F(X) = P(X <= x)
	- Joint distribution - multivariable version of PDF
- Collecting Data
	- Data sources
		- Online/existing
			- lots of existing sources for free and open-source data
		- Collected
			- Belmont reports
				- informed consent
				- beneficence - maximize benefit and minimize harm
				- justice
		- Web scraping
			- Python - beautifulsoup for html parsing
			- R - Rvest can do basic webscraping as well

















    <!--- MathJax stuff -->
    <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ TeX: { equationNumbers: {autoNumber: "all"} } });
    </script>