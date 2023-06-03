## Readme for Second AI Assignment (Pacman Project 2)

**Name**: Konstantinos Kanellakis 
**A.M.**: sdi2000064

This readme file provides an overview of the Pacman project, specifically focusing on questions Q1 to Q5. The project involves the implementation of various algorithms for Pacman agents.

### Q1. Reflex Agent

The reflex agent evaluates actions based on the following factors:
1. Distance to the closest dot
2. Distance to each ghost agent
3. Distance to each capsule

The evaluation function aims to prioritize actions that help Pacman eat the closest dot as quickly as possible. This is achieved by adding a fraction (1/min) to the "points" variable. Additionally, the evaluation function rewards actions that result in Pacman being farther away from ghosts to avoid losing. However, there are situations when Pacman has eaten a capsule and can kill ghosts, so actions that bring Pacman closer to ghosts are rewarded.

### Q2. Minimax

The minimax algorithm is implemented based on the provided pseudocode and lecture slides. Additionally, a depth variable is used to keep track of the expanded states when it is Pacman's turn.

### Q3. Alpha-Beta Pruning

Similar to the Minimax algorithm (Q2), Alpha-Beta Pruning (ABP) incorporates a and b variables to prune unnecessary states without affecting the result. The implementation follows the pseudocode from the lectures/slides, but with the use of `<` and `>` instead of `<=` and `>=`.

### Q4. Expectimax

The Expectimax algorithm is similar to Minimax (Q2), but with a change in the min function. Instead of calculating the optimal evaluation value, the average evaluation value of all actions is calculated. This assumption accounts for the fact that the min agents may not always make optimal decisions, leading to potential losses for Pacman (not in the autograder).

### Q5. Evaluation Function

The evaluation function in Q5 is similar to the one described in Q1. However, it is used to evaluate a state rather than an action. One difference is that there is no scenario in a state where Pacman is in a capsule since it would have been eaten. Therefore, the corresponding block of code has been commented out.
