from numpy import array
import chess
import sys
import numpy as np

class start():
    '''
    The job of this function is to be the 'spine' of self-play games between
    two agents during training
    '''

    def __init__(self, board):
        self.board = board

    def current_state(self, board):
        s = []
        for i in str(board):

            if i != " ":

                y = ' '.join(format(ord(i), 'b'))
                x = ""
                for i in y:
                    if i != " ": x += i
                x = int(x)
                s.append(x)
        s.append(1)
        a = array( s )
        return a

    def results(self, state, board_results):
        '''
        The job of this function is to check if the self-play game is finished or not
        '''
        if state.is_game_over() == True:

            if board_results =='*':
                return False, -1
            elif str(board_results)[2] == '0':
                return True, 'p2'
            elif str(board_results)[0] == '0':
                return True, 'p1'
            else:
                return True, -1

        else:
            return False, -1

    def start_self_play(self, player, temperature=1e-3):
            '''
            This starts the self-play when training the Model
            '''

            states, mcts_probs, live_agents = ['p1','p2'], [], []

            while True:
                move, probability_of_moves = player.get_action(self.board, temperature = temperature, return_prob = 1)

                states.append(self.current_state(self.board))

                mcts_probs.append(probability_of_moves)
                move = chess.Move.from_uci(str(move))
                self.board.push(move)

                end, winner = self.results(self.board, self.board.result())
                if end:
                    winner_outcome = np.zeros(len(live_agents))
                    if winner != -1:
                        winner_outcome[np.array(live_agents) == winner] = 1.0
                        winner_outcome[np.array(live_agents) != winner] = -1.0

                    player.reset_player()
                    return winner, zip(states, mcts_probs, winner_outcome)
