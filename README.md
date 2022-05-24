## Crossword solver

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

The program also needs a dictionary with all the available words. The current one is in catalan, but it may be replaced by another as long as if follows the same format. Note that it need to be encoded with ISO 8859-1


### How to execute
Download repository
```bash
git clone https://github.com/marti1999/Crossword-Solver.git
```
Install dependencies
```bash
pip install numpy
```

Run the script
```bash
python ./main.py
```

### Output
Once the execution has finished, the output should look like this (provided it uses the default crosswords)
```
CROSSWORD CB Backtracking

A   C   A   T   A   R
C   #   #   A   #   A
N   #   C   L   A   N
E   #   #   L   #   C
#   P   R   E   M   I
D   I   A   R   I   #

Backtracking:  0.016000032424926758 seconds
Total elapsed time:  0.017999887466430664 seconds


CROSSWORD CB Forward Checking

A   C   A   T   A   R
C   #   #   A   #   A
N   #   C   L   A   N
E   #   #   L   #   C
#   P   R   E   M   I
D   I   A   R   I   #

Forward Checking:  0.0010006427764892578 seconds
Total elapsed time:  0.0020024776458740234 seconds


CROSSWORD A Forward Checking

R   E   B   E   V   E   N   T   #   V   I   A
E   R   I   N   E   S   #   O   D   I   #   J
C   O   B   #   U   T   O   P   I   S   T   A
A   G   L   A   #   E   M   A   N   A   R   E
V   #   I   C   O   S   A   N   S   #   E   N
A   D   O   L   L   I   #   T   #   D   U   T
R   E   F   I   I   #   A   S   T   U   R   #
#   V   I   V   I   N   T   #   U   R   E   A
C   O   L   E   #   A   R   O   M   A   #   M
E   N   #   L   A   P   O   #   I   D   E   A
C   #   E   L   M   #   P   E   D   O   N   #
S   A   N   #   O   R   I   N   #   R   A   I

Forward Checking:  10.811723709106445 seconds
Total elapsed time:  12.819247484207153 seconds
```
