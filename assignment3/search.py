# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST


    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print(problem.getStartState())


    from game import Directions
    s=Directions.SOUTH
    w=Directions.WEST
    n=Directions.NORTH
    e=Directions.EAST
    path=[]
    visitedPoints=[]
    pathPoints=[]
    position=problem.getStartState()


    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors((5,5))

    #print "Am i there:",problem.isGoalState((5,4))
    pathPoints.append(problem.getStartState())
    path=dfsHelp(problem,path,position,pathPoints,visitedPoints)
    #print "Here is the path:",path
    return path

    util.raiseNotDefined()

test=0
def dfsHelp(problem,path,position, pathPoints,visitedPoints): #we are going to pass in the ordered pair for our posistion

    from game import Directions

    s=Directions.SOUTH
    w=Directions.WEST
    n=Directions.NORTH
    e=Directions.EAST

    sucessors=problem.getSuccessors(position) #will get all of our current ordered pair sucessors
    pathPoints

    if (problem.isGoalState(position)):
        return path
    else:
        for x in range(len(sucessors)):
            if ("South" in sucessors[x]) and (sucessors[x][0] not in visitedPoints):
                path.append(s)
                pathPoints.append(sucessors[x][0])
                visitedPoints.append(sucessors[x][0])
                return dfsHelp(problem,path,sucessors[x][0],pathPoints,visitedPoints)

        for x in range(len(sucessors)):
            if ("West" in sucessors[x]) and (sucessors[x][0] not in visitedPoints):
                path.append(w)
                pathPoints.append(sucessors[x][0])
                visitedPoints.append(sucessors[x][0])
                return dfsHelp(problem,path,sucessors[x][0], pathPoints,visitedPoints)


        for x in range(len(sucessors)):
            if ("East" in sucessors[x]) and (sucessors[x][0] not in visitedPoints):
                path.append(e)
                pathPoints.append(sucessors[x][0])
                visitedPoints.append(sucessors[x][0])
                return dfsHelp(problem,path,sucessors[x][0],pathPoints,visitedPoints)

        for x in range(len(sucessors)):
            if ("North" in sucessors[x]) and (sucessors[x][0] not in visitedPoints):
                path.append(n)
                pathPoints.append(sucessors[x][0])
                visitedPoints.append(sucessors[x][0])
                return dfsHelp(problem,path,sucessors[x][0],pathPoints,visitedPoints)



        path.pop()
        pathPoints.pop()
        return dfsHelp(problem,path,pathPoints[-1],pathPoints,visitedPoints)

    return path







def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from game import Directions

    s=Directions.SOUTH
    w=Directions.WEST
    n=Directions.NORTH
    e=Directions.EAST

    """ 1. start with a node with location
        1.5 check if the starting location is the goal

        2. make a queue with node as only element
        3. make an empty set for our visited nodes

        4. make a while loop that runs until we reach our goal
        5. pop our node from our queue
        6. add our node state to our queue

        7. have for loop that runs for all of neighbors
        8. make a child node that has the location, the sucessors, and the parents
        9. check if the child location is in the visited
        10. then check if the child location is the isGoal
        11. if it the goal run a loop that gets all of the parents
        12. if not the goal add the child to the queue """

    tile={'location':problem.getStartState()} #step 1: node

    if (problem.isGoalState(problem.getStartState())): #step 1.5
        return []

    boundary=util.Queue()
    boundary.push(tile) #step 2

    visited=set() #step 3

    while not boundary.isEmpty(): #step 4
        tile=boundary.pop() #step 5
        visited.add(tile['location']) #step 6

        sucessors=problem.getSuccessors(tile['location'])
        for neighbors in sucessors: #step 7

            child={'location':neighbors[0], 'direction':neighbors[1], 'parent':tile} #step 8
            if (child['location'] not in visited): #step 9

                if (problem.isGoalState(child['location'])): #step 10
                    path=[]
                    tile=child

                    while 'parent' in tile: #step 11
                        path.append(tile['direction'])
                        tile=tile['parent']

                    path.reverse()  #return the reverse because it will walk from children to parent and we need parent to children
                    return path #I tried to just reterun path.reverse() but i kept getting an error

                boundary.push(child) #step 12
    util.raiseNotDefined()










def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #basically the same thing as bfs just adding in cost
    from game import Directions

    s=Directions.SOUTH
    w=Directions.WEST
    n=Directions.NORTH
    e=Directions.EAST

    """ 1. start with a node with location but also add path cost
        1.5 check if the starting location is the goal

        2. make a queue with node as only element
        3. make an empty set for our visited nodes

        4. make a while loop that runs until we reach our goal
        5. pop our node from our queue
        6. add our node state to our queue

        7. have for loop that runs for all of neighbors
        8. make a child node that has the location, the sucessors, and the parents
        9. check if the child location is in the visited
        10. then check if the child location is the isGoal
        11. if it the goal run a loop that gets all of the parents
        12. if not the goal add the child to the queue """

    tile={'location':problem.getStartState(),'cost':0} #step 1: node add cost of 0 because we arent moving

    if (problem.isGoalState(problem.getStartState())): #step 1.5
        return []

    boundary=util.Queue()
    boundary.push(tile) #step 2

    visited=set() #step 3
    paths=[]

    while not boundary.isEmpty(): #step 4
        tile=boundary.pop() #step 5
        visited.add(tile['location']) #step 6

        sucessors=problem.getSuccessors(tile['location'])
        for neighbors in sucessors: #step 7



            child={'location':neighbors[0], 'direction':neighbors[1], 'cost': neighbors[2], 'parent':tile} #step 8 but add cost
            if (child['location'] not in visited): #step 9


                if (problem.isGoalState(child['location'])): #step 10

                    temp=[] #resets our temp to empty everytime we find a new path
                    tile=child
                    pathCost=0

                    while 'parent' in tile: #step 11
                        pathCost+=tile['cost']
                        temp.append(tile['direction'])
                        tile=tile['parent']

                    temp.reverse()  #return the reverse because it will walk from children to parent and we need parent to children
                    paths.append([temp,pathCost]) #adding this path combination to the list of possible paths

                boundary.push(child)
    #print paths

    min=paths[0][1]; #variable to find our minimum path length
    minPath=paths[0][0] #setting first path as current minimum path
    for x in range(len(paths)): #for loop to check all of our path combinations

        if (paths[x][1]<=min): #checks if our this path cost is less than our current stored minimum pathcost
            minPath=paths[x][0]

    return minPath #returns the mnimum path

 #tomorrow add a thing that is a flag checking if all possible neighbors are in sucessors





    util.raiseNotDefined()














def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    """
    sorry i comment my code a lot i really struggled with these projects so i used my comments to slowly walk myself through them

    i tried to get this version working with the objects but i couldnt ever seem to get the syntax correct

    step 1. were going to make a priority Queue
    step 2. were going to add our location our pathway and our cost to our node
    step 3. push our tile onto out queue along with the heuristic
    step 4. make while loop that runs until theres no more Options
    step 5. pop our temp and then add it to our variables
    step 6. check if that location is in our visited, if it is then skip, if not then add it
    step 7. check if were there if we are return our path
    step 8. if not then run through neighbors and make new nodes for each and add them to the boundary
    step 9. celebrate because we are done
    """

    boundary=util.PriorityQueue()   #priority queue for our boundary
                                    #priority queue will adjust lower heuristics automatically so dont have to worry about that
    visited=[]                      #our list for our visited points

    tile=[problem.getStartState(),[],0] #making an node that has the location, the current path taken, and the cost so far
    boundary.push(tile,heuristic(problem.getStartState(),problem))  #our tile is the item were passsing in and the priority is going to be our heuristic im pretty sure
                                                                    #the heuristic function takes a location and the problem

    while not boundary.isEmpty():  #will run until we have no more options :(

        temp=boundary.pop()  #get our first starting pop popped and adds it to all of our variables
        location=temp[0]
        pathway=temp[1]
        #print pathway
        cost=temp[2]

        if location not in visited: #check if the location is already in our explored if not then add it
            visited.append(location)

            if (problem.isGoalState(location)==True): #if were at our goal location return true
                return pathway

            else: #else add it to the priority queue then loop again with our new priority
                successors=problem.getSuccessors(location)

                for neighbors in successors: #then for all of our neighbors of our sucessors were gonna make nodes
                    tile = [neighbors[0],pathway+[neighbors[1]],cost+neighbors[2]]  #took me so long before i found my issue with pathway
                                                                                    #I still dont quite understand why i need to do that
                    boundary.push(tile,heuristic(neighbors[0],problem))

    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
