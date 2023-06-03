# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        if successorGameState.isWin():
            return 9999999999  # If sycessor's State is Win State go there!
        newPos = successorGameState.getPacmanPosition()
        prevFood = currentGameState.getFood().asList()
        newFood = successorGameState.getFood().asList()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        capsules = currentGameState.getCapsules()

        from util import manhattanDistance
        min = manhattanDistance(newPos, newFood[0])
        for x in newFood:
            dist = manhattanDistance(newPos, x)  # Find the manhattanDistance between sucessor's position and every dot
            if min > dist:
                min = dist  # Store the minimum distance
        points = 1 / min  # We know that higher is better for the evaluation function, so we prioritize the sucessorState \
        # with the minimum distance from food by giving him 1/min "points". That way the state which is closer to food will have more points!
        i = 0
        for x in successorGameState.getGhostPositions():
            dist = manhattanDistance(x, newPos)  # Find the manhattanDistance between sucessor's\
            # position and every ghost
            if dist < 2:  # If sucessor's State is near a ghost evaluate the State
                if newScaredTimes[i]:  # If ghost is scared reward the State more (+100) \
                    # as we earn more Score points if we eat the ghost
                    points += 10 * (1 / dist)  # We divide with dist as we want to give higher evaluation score\
                    # to states closer to eat a ghost.
                else:  # If ghost is NOT scared don't go near him
                    return -9999999999
            else:
                points += 1 / (dist * 10)  # Reward the States which are further from the ghosts \
                # (The impact on the points variable(*1/10) is smaller because it's not such a big deal, but we get better average score)
            i += 1  # Traversing the array newScaredTimes at the same time of traversing of getGhostPositions\
            # (The i ghost which we get the scared time is the same ghost we inspect in x)
        if newPos in capsules:  # We reward capsule States as we move more freely and can eat the ghosts
            points += 100
        elif bool(capsules):
            min = manhattanDistance(capsules[0], newPos)
            for x in capsules:
                dist = manhattanDistance(x, newPos)  # Find the manhattanDistance between sucessor's\
                # position and every capsule
                if min > dist:
                    min = dist  # Store the minimum distance
            if min < 3:  # Take into account the capsule minimum distance only when we pacman is very close to one
                points += 10 * 1 / min  # Next State is near a capsule. We reward such States following the method we mentioned earlier \
                # while we are giving some extra points to it (*10) as a capsule helps more than just eating a dot.
        return points + successorGameState.getScore()


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

        # The functions for minimax,max,min are formed just like the funcitons presented in the Lectures
        def max(state, depth, agent, succ):
            actions = state.getLegalActions(agent)  # Get all the legal actions of the agent
            maximum = -999999999  # Set minimum as something extremely low
            for x in actions:  # Explore all the actions
                v = minimax(state.generateSuccessor(agent, x), depth, succ)  # Get the minimax value of the action
                if v > maximum:
                    maximum = v  # Store the maximum value of all the actions
            return maximum  # Return maximum

        def min(state, depth, agent, succ):
            actions = state.getLegalActions(agent)  # Get all the legal actions of the agent
            minimum = 9999999999  # Set minimum as something extremely high
            for x in actions:  # Explore all the actions
                v = minimax(state.generateSuccessor(agent, x), depth, succ)  # Get the minimax value of the action
                if v < minimum:
                    minimum = v  # Store the minimum value of all the actions
            return minimum  # Return minimum

        def minimax(state, depth, agent):
            succ = agent + 1
            if state.isLose() or state.isWin() or depth == self.depth:
                return self.evaluationFunction(state)  # Evaluate the state and return the evaluation value
            if agent == 0:  # Behave to pacman as the max
                return max(state, depth, agent, succ)
            else:  # Behave to ghosts as min
                if succ == state.getNumAgents():  # If the last ghost is being examind right now,next will be pacman
                    succ = 0  # Time for pacman to play
                    depth += 1  # Update the depth variable if pacman is going to play next
                return min(state, depth, agent, succ)

        "*** YOUR CODE HERE ***"
        best = -9999999  # Set the best possible value to something really low (bigger is better as we examine max)
        next = Directions.STOP  # Set best action to STOP

        for action in gameState.getLegalActions(0):  # Examine all legal actions of the pacman to find which is better
            val = minimax(gameState.generateSuccessor(0, action), 0, 1)
            if best < val:  # Store the maximum minimax value and the best action which goes with it
                best = val
                next = action
        return next  # Return best action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """

        # The code is similar to minimax from q2 with some modifications(pruning) which I will point out by commenting on them
        def max(state, depth, agent, succ, a, b):
            actions = state.getLegalActions(agent)
            maximum = -999999999
            for x in actions:
                v = alphabeta(state.generateSuccessor(agent, x), depth, succ, a, b)
                if v > maximum:
                    maximum = v
                # Pruning-We used the > not the >= as showed in the class
                if v > b:  # No point on examimining other actions.
                    return v
                # Update a value
                if a < maximum:
                    a = maximum

            return maximum

        def min(state, depth, agent, succ, a, b):
            actions = state.getLegalActions(agent)
            minimum = 9999999999
            for x in actions:
                v = alphabeta(state.generateSuccessor(agent, x), depth, succ, a, b)
                if v < minimum:
                    minimum = v
                # Pruning-We used the < not the <= as showed in the class
                if v < a:  # No point on examimining other actions.
                    return v
                # Update b value
                if b > minimum:
                    b = minimum

            return minimum

        def alphabeta(state, depth, agent, a, b):
            succ = agent + 1
            if state.isLose() or state.isWin() or depth == self.depth:
                return self.evaluationFunction(state)
            if agent == 0:
                return max(state, depth, agent, succ, a, b)
            else:
                if succ == state.getNumAgents():
                    succ = 0
                    depth += 1
                return min(state, depth, agent, succ, a, b)

        "*** YOUR CODE HERE ***"
        best = -9999999
        next = Directions.STOP
        a1 = -9999999
        b1 = 9999999
        for action in gameState.getLegalActions(0):
            val = alphabeta(gameState.generateSuccessor(0, action), 0, 1, a1, b1)
            if best < val:
                best = val
                next = action
            # Update "a" value
            if a1 < val:
                a1 = val
        return next


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """

        # The code is similar to minimax from q2 with a modification(probability) which I will point out by commenting on them
        def max(state, depth, agent, succ):
            actions = state.getLegalActions(agent)
            maximum = -999999999
            for x in actions:
                v = expectiminimax(state.generateSuccessor(agent, x), depth, succ)
                if v > maximum:
                    maximum = v
            return maximum

        def min(state, depth, agent, succ):
            actions = state.getLegalActions(agent)
            sum = 0
            for x in actions:
                v = expectiminimax(state.generateSuccessor(agent, x), depth, succ)
                sum += v  # Getting the sum of v to calculate the probability later
            prob = sum / len(actions)  # We take the probability of the action x to be chosen
            return prob  # We basically return the average value of all the actions. Not the optimal value of the actions.

        def expectiminimax(state, depth, agent):
            succ = agent + 1
            if state.isLose() or state.isWin() or depth == self.depth:
                return self.evaluationFunction(state)
            if agent == 0:
                return max(state, depth, agent, succ)
            else:
                if succ == state.getNumAgents():
                    succ = 0
                    depth += 1
                return min(state, depth, agent, succ)

        "*** YOUR CODE HERE ***"
        best = -9999999
        next = Directions.STOP

        for action in gameState.getLegalActions(0):
            val = expectiminimax(gameState.generateSuccessor(0, action), 0, 1)
            if best < val:
                best = val
                next = action
        return next


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    # Return with the corresponding value if we lose or win
    if currentGameState.isWin():  # If State is Win choose this one
        return 9999999999999
    if currentGameState.isLose():  # If State is Lost DO NOT choose this one
        return -999999999999
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood().asList()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    capsules = currentGameState.getCapsules()
    positions = currentGameState.getGhostPositions()

    min = 999999999
    from util import manhattanDistance
    for food in newFood:
        dist = manhattanDistance(newPos, food)
        if min > dist:
            min = dist

    points = 1 / min  # We know that higher is better for the evaluation function, so we prioritize the sucessorState \
    # with the minimum distance from food by giving him 1/min "points". That way the state which is closer to food will have more points!
    i = 0
    for x in positions:
        dist = manhattanDistance(x, newPos)  # Find the manhattanDistance between sucessor's\
        # position and every ghost
        if dist < 2:  # If sucessor's State is near a ghost evaluate the State
            if newScaredTimes[i]:  # If ghost is scared reward the State more (+100/dist) \
                # as we earn more Score points if we eat the ghost
                points += 10 * (
                        1 / dist)  # We divide with dist as we want to give higher evaluation score to states closer to eat a ghost
            else:  # If ghost is NOT scared don't go near him
                return -9999999999
        else:
            points += 1 / (dist * 10)  # Reward the States which are further from the ghosts \
            # (The impact on the points variable(*1/10) is smaller because it's not as important as the distance to the closest dot)
        i += 1  # Traversing the array newScaredTimes at the same time of traversing of getGhostPositions\
        # (The i ghost which we get the scared time is the same ghost we inspect in x)

    # We are not taking into account the state where the capsule is in the same spot as pacman\
    # like we did in q1, because the capsule would have been eaten and so will be not in capsule list.\
    # That is a difference between evaluating State and Action.
    # if newPos in capsules:
    #     points += 100

    if bool(capsules):
        min = manhattanDistance(capsules[0], newPos)
        for x in capsules:
            dist = manhattanDistance(x, newPos)  # Find the manhattanDistance between sucessor's\
            # position and every capsule
            if min > dist:
                min = dist  # Store the minimum distance
            # We reward capsule States as we move more freely and can eat the ghosts
        if min < 3:
            points += 10 * 1 / min  # State is near a capsule. We reward such States following the method we mentioned earlier \
            # while we are giving some extra points to it (*10) as a capsule helps more than just eating a dot.
    return points + currentGameState.getScore()


# Abbreviation
better = betterEvaluationFunction
