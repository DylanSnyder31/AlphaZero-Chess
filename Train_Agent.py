import sys
from Reinforcement_Learning.game_state import TrainPipeline

if __name__ == "__main__":

    #Gets input from the user to decide how many games to train on
    games_to_play = int(str(sys.argv[1])[1:])
    #Loops through the main class

    main_learning = TrainPipeline()
    main_learning.run()
