# State Space Search


As we've covered, state space search is a general approach that can be applied to any problem domain that is deterministic, discrete, and static. In the reading from Russell and Norvig, they discuss a number of applications for this approach including route finding, VLSI layout, and automatic assembly sequencing. In class we examined how this approach could be applied to the water pitcher puzzle. In this homework, you will formulate a new problem so that state space search can be used. In addition, you will improve the efficiency of the state space search by recording all of the unique states that have been visited in a dictionary, and only adding unvisited states to the search queue.


## Targets/Proficiencies
---
- [ ] CL.1 navigate the command line
- [ ] CL.2 create/move/delete folders 
- [ ] CL.3 create SSH keys
---

- [ ] G.2 pull a repository
- [ ] G.3 commit and push to a repository
- [ ] G.5 writing Markdown

---
- [ ] PY.1	Python Programming (editing, compiling)
- [ ] PY.2	Python Debugging (your code, other's code)
- [ ] PY.3	Command-Line Python

---

- [ ] SS.2 State Spaces
- [ ] SS.3 Search Trees  
---

## Setup

* `git pull` the class repo to refresh contents
*  copy the project 2 folder into your own personal class repo, and add/commit/push the files into your repository.



## Borg and Crew 


This problem is a remix of the "Missionaries and Cannibals" problem that famous in AI because it was the subject of one of the [first papers](https://www.jstor.org/stable/pdf/3619658.pdf) that approached problem formation in a formal way.  It has its roots in the "Jealous Husbands" problem that dates to as far back as 800AD!  But let's modernize this a little bit:

Exactly Three (3) Members of the Federation and of Three (3) Borg find themselves isolated on a strange planet, and despite being enemies, have reached a temporary truce so they can return back to their ships.  However, there is a river in the way, along with a boat that can hold either one or two people. Find a way to get everyone to the other side of the river, without ever leaving a group of humans on either of the river outnumbered by the Borg (lest they become assimilated in to the Borg Hive Mind).

Note: you can treat travel in the boat as instantaneous - that is you don't have to model the passengers of the boat, only the occupants of each side of the river (and probably which side of the river the boat is on).

You'll find three files in the project directory from the course gitlab project: `search.py`, `pitcher.py` and `borg-puzzle.py`. 

The first file contains a general solution to state space search. It is based on four classes:  Queue,Node, Search, and ProblemState. Notice that the last class is completely abstract. This is intended to be an interface for how to formulate any appropriate problem for state space search. The `pitcher.py` file contains a concrete implementation of this abstract class.


You can execute the state space search on water pitcher problem:

`% python pitcher.py`  (the `%` denotes you are typing this in to the command line)

After testing this, go through the code and make sure you understand how it functions.

## Solving the Puzzle on Paper

First, on paper, formulate the humans-and-borg problem precisely, making only those distinctions necessary to ensure a valid solution.  Then draw a diagram of the complete state space showing the operators on the arcs. Given that the state space is so simple, why do you think people have a hard time solving this puzzle? 

The diagram and your answers to the above question should be submitted as part of your Write-Up

## Part 1: Solving in Python

Next, implement your formulation in the file `borg-puzzle.py`, using the `pitcher.py` implementation as a model.


## Part 2: Improving Search 

The search has a verbose mode which by default is turned off. 

* Turn on the verbose mode for an example of the water pitcher problem and observe how many states are being stored on the queue. 
* Update the search algorithm so that it uses a dictionary to store a representation of all of the unique states that have been visited.  The search should only add a node to the queue, if it is NOT already in this dictionary.   Russel & Norvig calls this "graph search". 
* In order to do this you'll need to create a NEW `search.py`.  Call it `improvedSearch.py`.   
* Verify that your new search works on both the pitcher problem and the borg problem. 
* Be sure to *analyze* and *compare* the performance of the original `search.py` against your implementation of graph search.  How many nodes are visited, how much faster does the algorithm run? You may want to learn how to time python code.

## Challenge Ideas:

* Apply state space search to a different problem!
__________________________________________________________________

## Answer to the question "Be sure to...want to learn how to time python code."

# State diagram
https://cs-gitlab.union.edu/memonm/memonm-csc-320/-/blob/main/project-2-borg/state_diagram.jpg

# Analyzing and comparing `search.py` and `graph implementation`.

## Time to reach the goal state
Searching through the improved search is much more efficient than the search algorithm itself. 
Using the time library in python, I was better able to provide my thesis for the observation that I made above. 
The runtime for the borg-puzzle using `search.py` and the graph method had the run times mentioned in the table below. 

| Search Type          | Run 1                 | Run 2                 | Run 3                 | Run 4                 | Run 5                 | Run 6                |
|----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|----------------------|
| Simple `search.py`   | 1.4546585083007812    | 1.443143606185913     | 1.427694320678711     | 1.4876556396484375    | 1.4548516273498535    | 1.3338687419891357   |
| using `graph` method | 0.0009989738464355469 | 0.0009984970092773438 | 0.0010497570037841797 | 0.0010333061218261719 | 0.0009984970092773438 | 0.000997781753540038 |


In order to compare both the runtimes, I calculated the average run time for each of the search methods in a tabular form

| Search Type          | Average time |  
|----------------------|--------------|
| Simple `search.py`   | 1.4364       |
| using `graph` method | 0.0010       |


According to these results, the improved runtime is 1,436.4 times better and faster than the search algorithm.

_**Note:** Previously, my Python file had some error while running so it showed 0.0 seconds to reach the goal. According to those results, graph method was infinitely better than the the simple search method._

## Nodes visited when using each method

### Simple `search.py` 
10,543 nodes were visited to reach the goal state of having 3 borgs and 3 humans on the other side of the river bank

### Searching using `graph` implementation
14 nodes were visited which are 10,543/14 = 753.07 times lesser than the nodes traveresed in case when `simple` search is used
