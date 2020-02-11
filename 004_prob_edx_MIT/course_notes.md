---
title: Probability - The Science of Uncertainty and Data
toc: true
---

Instructors: Prof. John Tsitsiklis, Dr. Sudarsan, Dr. Karene  
Platform: edX  
Part of: Course 1/4 in the MITx Micromaster Program in Statistics and Data Science  
Started on: January 28, 2020  
Course link: [https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2020/course/](https://courses.edx.org/courses/course-v1:MITx+6.431x+1T2020/course/)  


## Unit 0: Overview
- Goals for the course
	- Think probabalistically
	- Introduce tools for probability theory expressed mathematically
	- Bring probability skills to a level where they can be applied
- Why does probability play such a role in science today?
	- Complex systems often cannot be perfectly modeled and described
	- Information exists to reduce uncertainty

## Unit 1: Probability Models and Axioms
- Sample Space - all possible outcomes
	- Mutually exclusive
	- Collectively exhaustive
- Probability Laws
	- Event - subset of sample space
		- Probability can be assigned to events
	- Disjoint - two spaces that do not overlap
		- $\ A \cap B = \phi$
	- Axioms
		- Nonnegativity $P(A) >= 0$
		- Normal $P(\Omega) = 1$
		- Finite additivity $If \ A \cap B = \Phi, \ then \ P(A \cup B) = P(A) + P(B)$
	- Properties that follow the axioms
		- $P(A) <=1$
		- $P(\phi) = 0$
		- $P(A \cup B \cup C) = P(A) + P(B) + P(C)$
		- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
		- $P(A \cup B) \le P(A) + P(B)$
			- Union bound
- Examples
	- Discrete
	- Continuous
	- Steps
		1. Specify sample space
		2. Specify probability law
		3. Identify event of interest
		4. Calculate
- Discussion
	- Countable Additivity
		- If A1,A2,A3 is an infinite **sequence** of disjoint events, then additivity axiom holds
			- The elements of a unit square are "uncountable", whereas all the integers from 0 to infinity is "countable"
	- Mathematical Subtleties
- Interpretations of Probabilities
	- Frequencies
	- Description of beliefs
	- Betting strategies
	- Framework for analyzing penomena with uncertain outcomes
- Vocabulary
	- Sample space [$\Omega$] - space of possible outcomes
		- Also called the universal set
	- Event - subset of sample space
	- Empty set [$\phi$] - Set containing no outcomes
	- Disjoint - two spaces that do not overlap
		- $\ A \cap B = \phi$
	- Union [$A \cup B$] - contains all elements that are in at least one of the two sets
	- Intersection [$A \cap B$] - contains all elements that are in both sets
	- Complement [$A^c$] - the subset of the sample space that is not within the set
- Mathematical Background
	- Sets and De Morgan's laws
		- Set - collection of distinct elements
		- De Morgan's Laws
			- Allow us to go back and forth with unions and intersections
			- $(S \cap T)^c = S^c \cup T^c$
			- $S^c \cap T^c = (S \cup T)^c$
	- Sequences and their limits
		- Convergence criteria - For any $\epsilon > 0$, there exists a time where, after this time, elements of the sequence stay within the band $a \plusminus \epsilon$. This sequence has converged to $a$.
	- Infinite series
		- Monotonic - always converges and limit exists
			- Either finite or infinite
		- Sign flipping - limit exists if $\sum(\abs(a_i)) < \inf$
		- Geometric series - $\sum(a^i) = 1/(1-a)$ if $\abs(a)<1$
	- Sums with multiple indices
		- if sum(abs(all terms)) < infinity, then convergent and we can add in any order
			- if not satisfied, order can matter
	- Countable and uncountable sets
		- Countable
			- discrete
			- can be put in a 1-1 correspondance with positive integers
			- examples:
				- positive integers
				- integers
				- pairs of positive integers
				- rational numbers between 0 and 1
		- Uncountable
			- continuous
			- example:
				- any interval

## Unit 2: Conditioning and Independence
- Conditioning
	- Revising a model based on new information
	- Write this as P(A|B) - probability of A given B
	- $P(A|B) = P(A \cap B) / P(B)$
	- Conditional probabilities satisfy all the same axioms
	- Divide and Conquer Tools
		- Multiplication rule
			- $P(A \cap B) = P(B)P(A|B)$
			- Probability a composite event occurs is the probability the first event occurs * the probability the second event occurs given the first even occured
			- Can be generalized to n events by following the tree branches
		- Total probability theorem
			- If sample space is partitioned into $A_i$
				- $P(B) = \sum(P(A_i)P(B|A_i))$
			- Can be though of as a weighted average 
		- Bayes' rule
			- System of revising "beliefs", $P(A_i)$, over time given observations using conditional probabilities.
			- $P(A_i|B)=P(A_i \cap B) / P(B)$
			- $P(A_i|B)=P(A_i)P(B|A_i) / \sum(P(A_j)P(B|A_j))$ for $j$ observations
			- Bayesian inference
				- Initial beliefs
				- Model world
				- Draw conclusions about causes
				- Revise beliefs
- Independence
	- Independence of two events
		- Intuitive "definition": $P(B|A) = P(B)$
		- Better definition: $P(A \cap B) = P(A)P(B)$
		- Independence is not disjoint
		- If $A$ and $B$ are independent, $A$ and $B^c$ are independent
	- Conditional independence
		- same as regular independence subject to condition
		- independence does not imply conditional independence
	- Independence of a collection of events
		- Information on some of the events does not change probabilities of the rest of the events
		- $P(A_i \cap A_j \cap ...) = P(A_i)P(A_j)...$
	- Pairwise independence
		- independence of two events from each other
	- Reliability
		- Use De Morgan's laws to assess failure as complement of normal operation
	- The King's sibling puzzle
		- The king comes from a family of two children, what is the probability that his sibling is female?
			- 2/3, be careful of assumptions

- Vocabulary
	- Partition - split space into disjoint sets that span the space

















    <!--- MathJax stuff -->
    <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ TeX: { equationNumbers: {autoNumber: "all"} } });
    </script>