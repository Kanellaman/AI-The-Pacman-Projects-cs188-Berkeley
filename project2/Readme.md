# Project 2: Multi-Agent Pacman

This project involves creating agents for the game of Pacman that can handle multiple agents and incorporate adversarial search algorithms.

## Run Grader

Use of Python 3.6 is advised for the smooth execution of the program, but it can run with newer Python versions (It may need some modifications - NOT suggested).<br/>
To execute in the terminal:

```
python autograder.py
```


## Agents Implemented

The following agents are implemented for playing Pacman:

1. **Reflex Agent**
   - Description: A reflex agent chooses an action at each choice point by examining its alternatives via a state evaluation function.
   - Implementation: `ReflexAgent` class in `multiAgents.py`

2. **Minimax Agent**
   - Description: The minimax agent uses the minimax algorithm to make decisions by exploring the game tree and finding the optimal move.
   - Implementation: `MinimaxAgent` class in `multiAgents.py`

3. **Alpha-Beta Agent**
   - Description: The alpha-beta agent improves upon the minimax agent by using alpha-beta pruning to reduce the number of nodes that need to be evaluated.
   - Implementation: `AlphaBetaAgent` class in `multiAgents.py`

## Getting Started

To get started with the project, you can use the provided implementations of the agents and run them on the Pacman game. Each agent has a specific strategy for making decisions.

## Usage

To use the agents, you need to have the following code available:

- `ReflexAgent`: Implements a reflex agent that uses a state evaluation function to choose actions.
- `MinimaxAgent`: Implements a minimax agent that uses the minimax algorithm to make decisions.
- `AlphaBetaAgent`: Implements an alpha-beta agent that improves upon the minimax agent using alpha-beta pruning.

Please refer to the code provided in the project for the complete implementations of the agents.

## Additional Notes

- The agents utilize different search algorithms and evaluation functions to make decisions.
- The `GameState` class provides information about the current state of the game, including the positions of agents and game elements.
- The game involves multiple agents, including Pacman and ghosts, each with different goals and behaviors.

## Resources

If you need additional information or resources related to the Pacman projects, you can [mail me](mailto:kanellakhskostas@gmail.com) or refer to the official CS188 course materials from UC Berkeley:

- [CS188 Pacman Projects](https://inst.eecs.berkeley.edu/~cs188/sp22/project2/)
