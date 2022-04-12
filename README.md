This program, written with Python and Numpy library, is able to solve a crossword with a given word dictionary.
Whilst it approaches the main task by using a Backtracking algorythm, the execution time is further improved by also using Forward Checking and MRV, thus simplifying the Constraint Satisfaction Problem.  
It also features a somewhat probabilistic algorythim. The words in the dictionary are randomly sorted and the algorythom runs for N seconds. If it has not finished in the given time, a new sorting is made.



The input crossword file must look like this:
```
0	0	0	0	0	0
0	#	#	0	#	0
0	#	0	0	0	0
0	#	#	0	#	0
#	0	0	0	0	0
0	0	0	0	0	# 
```
- 0 indicates a character
- \# indicates a separator
