# Project 1: Search Algorithms

This project implements search algorithms to find optimal paths for Pacman through mazes. The goal is to search the deepest nodes in the search tree first and return a list of actions that reaches the goal.

## Run Grader

Use of python3.6 is advised for the smooth execution of the program, but it can run with newer python version (It may be need some modifications-NOT suggested).<br/>
To execute in terminal:
```
python autograder.py
```

## Algorithms Implemented

The following search algorithms are implemented:

1. **Depth-First Search**
   - Algorithm: Depth-first search (DFS)
   - Description: Search the deepest nodes in the search tree first.
   - Implementation: `depthFirstSearch(problem)`

2. **Breadth-First Search**
   - Algorithm: Breadth-first search (BFS)
   - Description: Search the shallowest nodes in the search tree first.
   - Implementation: `breadthFirstSearch(problem)`

3. **Uniform Cost Search**
   - Algorithm: Uniform cost search (UCS)
   - Description: Search the node of least total cost first.
   - Implementation: `uniformCostSearch(problem)`

4. **A* Search**
   - Algorithm: A* search (A-Star)
   - Description: Search the node that has the lowest combined cost and heuristic first.
   - Implementation: `aStarSearch(problem, heuristic=nullHeuristic)`

## Getting Started

To get started with the project, you can use the provided implementations of the search algorithms and run them on specific problem instances. Each algorithm takes a `SearchProblem` as input and returns a list of actions that leads Pacman to the goal.

## Usage

To use the search algorithms, you need to have the following code available:

- `depthFirstSearch(problem)`: Implements depth-first search algorithm.
- `breadthFirstSearch(problem)`: Implements breadth-first search algorithm.
- `uniformCostSearch(problem)`: Implements uniform cost search algorithm.
- `aStarSearch(problem, heuristic=nullHeuristic)`: Implements A* search algorithm with an optional heuristic function.

Please refer to the code provided in the project for the complete implementations.

## Additional Notes

- The search algorithms utilize a stack, queue, or priority queue to manage the search frontier.
- The `SearchProblem` class defines the search problem and provides necessary methods like `getStartState()`, `isGoalState()`, and `getSuccessors()`. Ensure that you have implemented this class correctly.

## Resources

If you need additional information or resources related to the Pacman projects, you can [mail me](mailto:kanellakhskostas@gmail.com) or refer to the official CS188 course materials from UC Berkeley:

- [CS188 Pacman Projects](https://inst.eecs.berkeley.edu/~cs188/sp22/project1/)

