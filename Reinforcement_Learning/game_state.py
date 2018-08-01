from __future__ import print_function
from collections import defaultdict, deque

import chess
import random
import numpy as np

from Reinforcement_Learning.Monte_Carlo_Search_Tree.self_play import start
from Reinforcement_Learning.Monte_Carlo_Search_Tree.MCTS_main import agent_MCTS
from Reinforcement_Learning.Monte_Carlo_Search_Tree.deep_structure import Neural_Network

class Train_Network():

    def __init__(self):
        self.board = chess.Board()
        self.play = start(self.board)

        # Hyperparameters
        self.learning_rate = 2e-3
        self.multiplier = 1.0
        self.temperature = 1.0
        self.playout = 400
        self.Cpuct_value = 5

        self.batch_size = 512
        self.batch_number = 1500
        self.play_batch_size = 1
        self.buffer = deque(maxlen=10000)

        self.epochs = 5
        self.goal = 0.02
        self.check = 50
        self.win = 0.0
        self.mcts_play = 1000

        ''' Change to FALSE if you want to start training from scratch '''
        if True:
            self.Neural_Net = Neural_Network()
        else:
            # start training from a new policy-value net
            self.Neural_Net = Neural_Network()

        self.agent = agent_MCTS(self.Neural_Net.policy_value_fn, is_selfplay=1)

    def data_storing(self):
        '''
        The goal of this function is to loop, and collect the data
        from the matches of self-play
        '''
        for i in range(1):
            winner, data = self.play.start_self_play( self.agent, temperature=self.temperature )
            data = list(data)[:]

            self.episode_len = len(data)
            self.buffer.extend(data)

    def update(self):
        '''
        The job of this function is to update the Neural Network, in order for it to
        learn and get better over time
        '''
        small_batch = random.sample(self.buffer, self.batch_size)
        states = [data[0] for data in small_batch]
        probabilities = [data[1] for data in small_batch]
        winner_batch = [data[2] for data in small_batch]
        old_probabilities, old_values = self.Neural_Net.policy_value(states)

        for i in range(self.epochs):
            loss, entropy = self.Neural_Net.train_step(states, probabilities, winner_batch, self.learning_rate*self.multiplier)
            new_probabilities, new_values = self.Neural_Net.policy_value(states)
            l = np.mean(np.sum(old_probabilities * ( np.log(old_probabilities + 1e-10) - np.log(new_probabilities + 1e-10)), axis=1) )

            if l > self.goal * 4:
                break

        if l > self.goal * 2 and self.multiplier > 0.1:
            self.multiplier /= 1.5

        elif l < self.goal / 2 and self.multiplier < 10:
            self.multiplier *= 1.5

        return loss, entropy

    def policy_evaluate(self):
        '''
        The job of this function is to Evaluate the current Neural Network, and
        test to see if it is 55% better than the current best Neural Network.

        This is done in AlphaZero.
        '''

        current_agent = agent_MCTS(self.Neural_Net.policy_value_fn)
        best_agent = agent_MCTS(self.Neural_Net.policy_value_fn)

        dic_win = defaultdict(int)
        for i in range(10):
            winner = self.game.start_play(current_agent, best_agent, start_player=i % 2)
            dic_win[winner] += 1

        return ( 1.0*( dic_win[1] + 0.5*dic_win[-1] ) / 10 )


    def run(self):
        '''
        The job of this function is to bring everything together and be the 'meeting grounds'
        for all of the other functions and run them simultaneously, training the model
        '''

        for i in range(self.batch_number):
            self.data_storing(self.size)

            if len(self.buffer) > self.batch_size:
                loss, entropy = self.update()
            self.Neural_Net.save_model('./best_policy.model')

            if (i+1) % self.check == 0:
                win_ratio = self.policy_evaluate()
                self.Neural_Net.save_model('./current_policy.model')

                if win_ratio > self.win:
                    self.win = win_ratio

                    if (self.win == 1.0 and self.mcts_play < 5000):
                        self.mcts_play += 1000
                        self.win = 0.0

if __name__ == '__main__':
    training_pipeline = Train_Network()
    training_pipeline.run()
