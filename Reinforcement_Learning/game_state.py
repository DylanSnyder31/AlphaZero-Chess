import chess
from Reinforcement_Learning.Monte_Carlo_Search_Tree.MCTS_main import MCTS

class State():

    def fresh_state(self, games_to_play):
        board = chess.Board()
        print(games_to_play)
        print(board)
        print(board.fen())
        monte_carlo = MCTS(str(board.fen()))
        monte_carlo.resource_limits()
