## Readme for First AI Assignment (Pacman Project 1)

**Name**: Konstantinos Kanellakis
**A.M.**: sdi2000064

This readme file provides an overview of the Pacman project, specifically focusing on questions Q1 to Q8. The project is based on the pseudocode presented in the lecture about graph search algorithms. 

### Q1. Depth First Search

In this question, we implement depth-first search (DFS) using a stack data structure. The algorithm follows a Last-In-First-Out (LIFO) policy. We visit and delete the last node inserted into the list.

### Q2. Breadth First Search

For Q2, we implement breadth-first search (BFS) using a queue data structure. The algorithm follows a First-In-First-Out (FIFO) policy. We visit and delete the node that was inserted first into the list.

### Q3. Uniform Cost Search

Uniform cost search (UCS) is implemented in Q3. This algorithm utilizes a priority queue, which ensures that we visit the node with the lowest cost first.

### Q4. A* Search

Similar to UCS, A* search (Q4) also employs a priority queue. However, in addition to the cost, the priority is determined by the heuristic function's value for each node. The algorithm aims to find the optimal path to the goal state.

### Q5. Finding All Corners

The state representation for this question includes the current location (x, y) and a list of remaining corners to find. The starting state is set to the node where Pacman begins, along with the list of corners. The function `getStartState()` returns this information.

To determine if the goal state is reached, we check if there are no more corners left in the current state's corner list. This information is obtained by calling the function `isGoalState()`.

To generate the successors of a node, we explore every possible direction: north, south, east, and west. We verify if each direction leads to a wall to avoid going in that direction. If there is no wall, we add the node to the successors list. Additionally, if the next node is a corner that hasn't been visited yet, we remove it from the corner list. The function `getSuccessors()` implements this algorithm.

### Q6. Corners Problem Heuristic

For the corners problem, the heuristic function evaluates the Manhattan distance from the current node to each unvisited corner. The heuristic includes the minimum Manhattan distance among the unvisited corners. This approach ensures that the heuristic does not overestimate the actual cost of the solution and is admissible. Furthermore, as we move closer to the corners and the goal state, the Manhattan distance overall decreases, making the heuristic consistent.

### Q7. Eating All the Dots

This question resembles the Traveling Salesman Problem (TSP). However, we don't need to return to the starting position. Thus, the goal is to find the maximum distance between the current state and any uneaten dot. To achieve this, we calculate the Maze distance for each dot from the current state and select the maximum distance. The Maze distance is preferred over the Manhattan distance as it takes into account the maze layout and avoids considering walls.

### Q8. Suboptimal Search

In Q8, to find the path, we utilize Uniform Cost Search (UCS) as the algorithm greedily chooses the next state. If there is still uneaten food, indicating that the goal state hasn't been reached, the function returns False. If there is no uneaten food left, the function returns True, indicating the goal state has been reached.

