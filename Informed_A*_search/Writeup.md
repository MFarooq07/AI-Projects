## Experiment Results

| Problem  | A*(tiles) | A*(dist) | A*(dist time) | A*(tiles time) |
|----------|-----------|----------|---------------|----------------|
|A         | 2         | 2        | 0.0010295     | 0.0011528      |
|B         | 8         | 6        | 0.009268      | 0.01266        |
|C         | 17        | 8        | 0.02907       | 0.03042        |
|D         | 47        | 23       | 0.08142       | 0.08771        |
|E         | 47        | 21       | 0.08          | 0.103          |
|F         | 101       | 17       | 0.21          | 0.23           |
|G         | 379       | 53       | 1.07          | 1.11           |
|H         | 3528      | 201      | 7.81          | 8.68           |
|          |           |          |               |                |

### Analysis and Explanation
In summary, the results show that the Manhattan distance heuristic (A*(dist)) generally outperforms the tiles-out-of-place 
heuristic (A*(tiles)) in terms of the number of nodes visited. This is because the Manhattan distance heuristic provides 
a better estimation of the true cost to reach the goal state, which guides the search more efficiently, especially in 
larger and more complex problem instances.

Considering the time taken by each of the search methods, we can say that A*(dist) excels in this context because of its
ability to provide more accurate guidance, effective pruning, and better performance in complex scenarios. A*(tiles) may
struggle due to its less informative heuristic, which can result in longer search times for each puzzle instance.
