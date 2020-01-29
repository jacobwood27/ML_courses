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
	- Event - subset of sample space
	- Empty set [$\phi$] - Set containing no outcomes
	- Disjoint - two spaces that do not overlap
		- $\ A \cap B = \phi$
	- Union [$A \cup B$] - contains all elements that are in at least one of the two sets
	- Intersection [$A \cap B$] - contains all elements that are in both sets
	- Complement [$A^c$] - the subset of the sample space that is not within the set





    <!--- MathJax stuff -->
    <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ TeX: { equationNumbers: {autoNumber: "all"} } });
    </script>