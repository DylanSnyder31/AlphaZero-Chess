import chess
import random
'''
This is the MCTS algorithm implemented in Python

The differences between this MCTS (The Alphazero algorithm) and a
standard implementation is as follows:

    1. Rollouts are replaced by fetching predictions from the Neural Network
    2. The equation, PUCT, replaces UCB1
'''

class MCTS():
    '''
    NEED TO RETURN A MOVE:

    Self-play. The best current player αθ∗, as selected by the evaluator, is used to  generate data. In each iteration, αθ∗ plays 25,000 games of self-play, using 1,600  simulations of MCTS to select each move (this requires approximately 0.4 s per search). For the first 30 moves of each game, the temperature is set to τ =   1;  this selects moves proportionally to their visit count in MCTS, and ensures a diverse set of positions are encountered. For the remainder of the game, an infinitesimal temperature is used, τ→ 0. Additional exploration is achieved by adding Dirichlet noise to the prior probabilities in the root node s0, specifically P(s, a) =   (1 −   ε)pa +   εηa, where η ∼   Dir(0.03)  and  ε =  0.25; this noise ensures that all moves may be tried, but the search may still overrule bad moves. In order to save computation, clearly lost games are resigned. The resignation threshold vresign is selected automatically to keep the fraction of false positives (games that could have been won if AlphaGo had not resigned) below 5%. To measure false posi-tives, we disable resignation in 10% of self-play games and play until termination.
    '''

    def __init__(self, state):
        self.visit_history = []

        self.iterations = 0

        #This is current state of the board in real play
        self.game_state = state

        #This will be the state that changes throughout the observations of the Tree
        self.observing_state = state

        #The dictionary for edges
        self.edges = {}
        self.edges[self.game_state, 0] = None

        #The dictionary for Nodes
        self.nodes = {}

        #Define what layer the observation is currently in
        self.layer = 1

    def resource_limits(self):

        #Expands if the tree is just one node (The base positions)
        if len(self.edges) == 1:
            self.simulate_leaf_node()

        #This will loop until MCTS has ran for 800 iterations
        while self.iterations <= 1600:
            #Since this is a new iteration, the history is new as well
            self.visit_history = []

            #Run one iteration of the MCTS
            self.search_for_leaf_node()
            #Update the iteration number
            self.iterations += 1

    def search_for_leaf_node(self):
        #This is the Selection step
        #The goal of this step is to find a leaf node, using the PUCT equation
        while self.if_leaf_node() == False:

            #Get the branch with the highest Q + U
            #Sadly this will take O(n) time, because the list will not have been sorted
            largest_value = 0
            for i in self.list_of_values:

                if i > largest_value:
                    largest_value = i

            #Adds the final edge to the history
            self.visit_history.append([self.observing_state, largest_value, self.layer -1])
            #Change the observing state to the state with the highest Q + U
            self.observing_state = self.edges[self.observing_state, self.layer - 1][largest_value][4]

            #We traversed down one more layer through the Tree
            self.layer += 1

    def if_leaf_node(self):
        '''
        This checks the nodes in the Edge Dictionary;
        If that Node has no edges, then it must be a Leaf Node
        else it cannot be a Leaf Node
        '''

        try:
            self.list_of_values = list(self.edges[self.observing_state, self.layer - 1])
            return False
        except TypeError:

            self.simulate_leaf_node()

    def simulate_leaf_node(self):
        #This will Call the NN in order to get the V and P values for the node

        '''
        CALL THE DEEP NEURAL NETWORK
        Do we do this before or after or during getting the children?
        '''
        #self.V, self.P =
        self.V, self.P = 10, .3

        #Expand the Leaf with children
        #Don't visit the children
        self.expand_leaf_node()


    def expand_leaf_node(self):

        #Gets the board for the current state
        board = chess.Board(self.observing_state)

        #Loops through each legal move from this state
        for i in list(board.legal_moves):
            #This is the legal move chosen
            move = chess.Move.from_uci(str(i))

            #Move the board to that state
            board.push(move)

            #Get the state after the move
            state_after_move = board.fen()

            #Undo the Move
            board.pop()

            #Adds the Edge connecting to the new Leaf Node
            self.edges[state_after_move, self.layer] = None

            #Adds a dictionary so we can add the possible moves
            if self.edges[self.observing_state, self.layer - 1] == None:
                self.edges[self.observing_state, self.layer - 1] = {}
            probability = self.calculate_U()

            #Adds the legal moves to the tree, underneath the current node
            #Assigns their values 0 because they have never been explored
            self.edges[self.observing_state, self.layer - 1][probability] = [ 0, 0, 0, self.P, state_after_move ]

        #backpropagate the values up the tree
        self.backpropagation()


    def backpropagation(self):
        #This will return all values up the hierarchy
        for i in self.visit_history:
            U = self.calculate_U()
            print(self.edges)
            print(U)
            #Re-calculates the Q + U and re-key the dictionary
            print("jjjjjjjj")
            print(i[0])
            value = self.edges[i[0], i[2]][i[1]]

            self.edges[i[0], i[2]][int(U)] = value
            self.edges[i[0], i[2]].pop(i[1])
            # i = [obverved state, index_of_highest (for this state)]
            # edge = self.edge[observed_state][index_of_highest
            edge = self.edges[i[0], i[2]][int(U)]
            # edge is now equal to the value of the edge
            # edge = [N, W, Q, P, state]

            # Adds one for the N value,
            # (the # of times this action has been taken)
            edge[0] += 1

            # Adds V (from the Neural Network) to W
            # (The total value)
            edge[1] += self.V

            # Recalculates Q with W/N
            # Q is the mean value
            edge[2] = edge[1] / edge[0]

    def calculate_U(self):
        # This calculates the value U
        # The equation for U is on the top right of page 8 in their first paper
        # ( https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ )
        total_number = 0
        for i in self.visit_history:
            #[self.observing_state, self.index_of_highest, self.layer]
            total_number = self.edges[ (i[ 0 ], i[ 2 ]) ][ i[ 1 ]][ 0 ]

        total_number = (total_number**.5)/ (1)
        if self.P * total_number in self.edges[self.observing_state, self.layer -1]:
            probability = self.P * random.random() * 1000
        else:
            probability = self.P * total_number *100
        # In the paper they multiply by Cpuct, and I couldn't find the value of
        # Cpuct, but multiplying everything by the same number will not do anything, just
        # cause inflation/deflation of the numbers; So I do not multiply by Cpuct

        return probability
