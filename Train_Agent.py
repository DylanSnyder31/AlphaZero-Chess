import sys
from Reinforcement_Learning.game_state import TrainPipeline

if __name__ == "__main__":

    #Gets input from the user to decide how many games to train on
    games_to_play = int(str(sys.argv[1])[1:])
    #Loops through the main class

    main_learning = TrainPipeline()
    main_learning.run()







'''

What I need:
    1. Have a loop to run algorithm until specified game limit/time limit
        Algorithm:
            1. Game state working
                A. This can update throughout the game, use python-chess (For lots of the functionality), and is compressed

            2. MCTS Algorithm
                A. Modified to the AlphaZero specifications

                B. Deep Neural Network
                    A. 42 Layer structure
                        I. Convolutional Layer
                        II. 40 Residual Layers
                        III. The Heads
                            1. The Value Head
                            2. The Polcy Head

                C. Decide the conclusion of the game
                    A. Update Variables based on win/draw/loss for which side
                        I. This is the Optimize Network step in the Cheat Sheet

                D. Decide if Evaluating Network is necessary (once every X amount of games)
                    A. Play X amount of games against best_network and current_network
                    B. Decide if updating best_network is correct

                E. Get fresh Game state

                F. LOOP

File structure:

    Train_Agent - This will be #1 - Looping the algorithm for a specified period of time (Get the command line commands to work)

    FOLDER Reinforcement_Learning: - This will contain the whole algorithm as we know it

        Game_state.py - This will handle the ALL manipulation of game states and will create fresh game states (in different functions)

        FOLDER MCTS Algorithm: - This will contain the files dedicated to the Tree

            MCTS.py - Alphazero implementation of the algorithm; this will be the 'Spine' of the algorithm

            deep_structure.py - the structure of the network

            convolutional_layer.py - The convolutional layer

            Residual_layer.py - the Residual layer

            Value_head.py - The value Head

            Policy_head.py - The Policy Head

        Optimize_network.py - optimizes the network with the game winner/loser/tie and all the data

        #Checks if this is needed in OPtimze_network.py
        Evaluate_network.py - Evaluates the Network
'''
