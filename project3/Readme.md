## Readme for Fourth AI Assignment (Pacman Project 3)

**Name**: Konstantinos Kanellakis
**A.M.**: sdi2000064

This readme file provides an overview of the Pacman project, specifically focusing on questions Q1 to Q8. The project involves implementing logic-based solutions for various problem scenarios in Pacman.

### Q1. Logic Warmup

In Q1, Expr instances are used to express logical sentences. The logical operators are used as presented in the project's instructions. The `findModel()` function returns the model satisfying the logical sentences. The `findModelCheck()` function is updated to match the intended return statement. The `entails()` function implements the theorem presented in class (Chapter 8). Additionally, the `plTrueInverse()` function is implemented as instructed.

### Q2. Logic Workout

For Q2, different scenarios are addressed based on the list of literals (A, B, C, D, Z, Y, ...):
- For at least one `Expr` instance to be `True`, the disjunction of literals A, B, C, ... is used.
- For at most one `Expr` instance to be `True`, the sentence (~A | ~B) & (~A | ~C) & (~B | ~C) & ... is used. This ensures that only one literal can be `True`.
- For exactly one `Expr` instance to be `True`, a combination of the previous two functions is used.

### Q3. Pacphysics and Satisfiability

In Q3, modifications are made to the `pacmanSuccessorAxiomSingle()` function to ensure that Pacman can only move to the next step (x, y+1 or x+1, y or x, y-1 or x-1, y) if it is currently at position x, y and there are no walls blocking the way. The `pacphysicsAxioms()` function creates rules to limit the search for Pacman's possible positions based on the Pacphysics principles and the fact that Pacman can only be at one location at a time. The `checkLocationSatisfiability()` function uses the previous functions to determine if Pacman is possibly at (x1, y1) or not at (x1, y1) starting from (x0, y0). The `pacphysicsAxioms()` function is called twice, once for t=0 (start state) and once for t=1 (successor state). Based on the knowledge base and the possibility of Pacman being at (x1, y1) or not (model1 and model2), the results are returned.

### Q4. Path Planning with Logic

Q4 involves finding a path for Pacman to complete the maze. The goal is to obtain all possible locations at every time t. If the coordinates (x, y) corresponding to the goal's coordinates match the knowledge base (Pacman is at the goal state) and its restrictions, the `model` variable contains the path Pacman needs. The path and actions list are returned.

### Q5. Eating All the Food

Q5 is similar to Q4, but the goal is to eat every dot. The knowledge about the food at different timestamps is added and updated. The successor states are checked differently, ensuring that the knowledge about the food at time t is also given to time t+1. Further details can be found in the code comments.

### Q6. Localization

Q6 focuses on localization. The entailments about Pacman's position are derived from previous questions and used to update the possible locations of Pacman based on new information.

### Q7. Mapping

Similar to Q6, but instead of the starting position, the positions of walls are unknown. The solution follows a similar template as Q6, with modified `Exprs` to match the problem's requirements. Instead of finding possible locations, the map of the Pacman environment is updated with -1s, 0s, and 1s.

### Q8. SLAM

Q8 combines the problems from Q6 and Q7. The solution is a combination of the solutions from Q6 and Q7, finding both possible locations of Pacman and the correct map of the maze.