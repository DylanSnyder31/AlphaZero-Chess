import numpy as np

#Import all of the necessary Torch dependencies
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as functional
from torch.autograd import Variable

from Reinforcement_Learning.Monte_Carlo_Search_Tree.self_play import start

'''
This file is the Deep Neural Network used in Alphazero, implemented in Pytorch.

The Architecture is: input (the board state)-> convolutional layer -> 40 residual layers -> value and policy heads
'''
class Neural_Network_Architecture(nn.Module):
    '''
    This class will setup the Neural Network with common layers that are
    repeatedly used in the architecture of AlphaZero's Deep Neural Network
    '''
    def __init__(self):
        super(Neural_Network_Architecture, self).__init__()

        #Initializes the common layers
        self.conv1 = nn.Conv2d(4, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        self.act_conv1 = nn.Conv2d(128, 4, kernel_size=1)
        self.val_conv1 = nn.Conv2d(128, 2, kernel_size=1)

        self.act_fc1 = nn.Linear(72, 18)
        self.val_fc1 = nn.Linear(36, 64)
        self.val_fc2 = nn.Linear(64, 1)

    def forward(self, current_state):
        #Gets the output of the two heads (policy and value)

        out = functional.relu(self.conv1(current_state))
        out = functional.relu(self.conv2(out))
        out = functional.relu(self.conv3(out))

        pol_out = functional.relu(self.act_conv1(out))
        pol_out = pol_out.view(-1, 72)
        pol_out = functional.log_softmax(self.act_fc1(pol_out))

        val_out = functional.relu(self.val_conv1(out))
        val_out = val_out.view(-1, 36)
        val_out = functional.relu(self.val_fc1(val_out))
        val_out = functional.tanh(self.val_fc2(val_out))

        return pol_out, val_out


class Neural_Network():
    '''
    The function of this class is to provide the functionality
    of the Neural Network, with the residual and convolutional layers
    '''
    def __init__(self, training=True):
        self.penalty = 1e-4
        #Training agent set to use a GPU and
        #playing against the agent is set to use a CPU
        self.training = training

        if self.training == True:
            self.Neural_Network_Architecture = Neural_Network_Architecture().cuda()
        else:
            self.Neural_Network_Architecture = Neural_Network_Architecture()

        self.optimizer = optim.Adam(self.Neural_Network_Architecture.parameters(), weight_decay=self.penalty)

        '''Change this to FALSE if you don't want to load the past data'''
        if True:
            print("LOADING IN PAST DATA")

            data_NN = torch.load(r'C:\Users\Dylan Snyder\Desktop\Machine_Learning_Ches\Reinforcement_Learning\Monte_Carlo_Search_Tree\best_policy.model', map_location=lambda storage, loc: storage)
            self.Neural_Network_Architecture.load_state_dict(data_NN)

            print("LOAD COMPLETE")
            print()

    def state_score(self, board):
        '''
        The job of this function is to get the 'score' for each state
        '''
        list_of_tuples = []
        tuple = []
        index = 0

        #This is the training state, coded and reshaped in order to fit into the Neural Network
        reshaped_state = np.ascontiguousarray( start(board).current_state( board ).reshape(-1, 4, 6, 3) )

        #Gets all of the possible legal moves from this current state
        legal_positions = list(board.legal_moves)

        if self.training == True:
            log_act_probs, value = self.Neural_Network_Architecture( Variable( torch.from_numpy(reshaped_state) ).cuda().float() )
            act_probs = np.exp(log_act_probs.data.cpu().numpy().flatten())

        else:
            log_act_probs, value = self.Neural_Network_Architecture( Variable( torch.from_numpy(reshaped_state) ).float() )
            act_probs = np.exp(log_act_probs.data.numpy().flatten())

        '''
        Algorithm in order to chanage the data into a usuable format
        '''
        for i in legal_positions:
            tuple.append(i)
            try:
                tuple.append(act_probs[index])
            except IndexError:
                tuple.append(act_probs[2])
            list_of_tuples.append(tuple)
            tuple = []
            index += 1

        return list_of_tuples, act_probs

    def train_network(self, group_of_states, probabilities, winner, learning_rate):
        '''
        The job of this function is to train the Neural Network, so it learns over time
        and can adjust it's parameters in order to make better 'judgements'
        '''
        self.optimizer.zero_grad()
        #Set the learning rate of the Network
        set_learning_rate(self.optimizer, learning_rate)

        if self.training == True:
            group_of_states = Variable(torch.FloatTensor(group_of_states).cuda())
            probabilities = Variable(torch.FloatTensor(probabilities).cuda())
            winner = Variable(torch.FloatTensor(winner).cuda())
        else:
            group_of_states = Variable(torch.FloatTensor(group_of_states))
            probabilities = Variable(torch.FloatTensor(probabilities))
            winner = Variable(torch.FloatTensor(winner))

        log_act_probs, value = self.Neural_Network_Architecture(group_of_states)
        value_loss = functional.mse_loss(value.view(-1), winner)
        policy_loss = -torch.mean(torch.sum(probabilities*log_act_probs, 1))
        loss = value_loss + policy_loss

        loss.backward()
        self.optimizer.step()

        entropy = -torch.mean( torch.sum( torch.exp(log_act_probs) * log_act_probs, 1 ) )

        return loss.data[0], entropy.data[0]

    def move_probabilities(self, group_of_states):
        '''
        The job of this function is to take a bunch of states, and
        return the probability of taking each state
        '''
        if self.training == True:
            group_of_states = Variable(torch.FloatTensor(group_of_states).cuda())
            log_act_probs, value = self.Neural_Network_Architecture(group_of_states)
            probabilities = np.exp(log_act_probs.data.cpu().numpy())

            return probabilities, value.data.cpu().numpy()
        else:
            group_of_states = Variable(torch.FloatTensor(group_of_states))
            '''
            The next two lines of code are repeated from above, but are needed because the
            return is different if using a GPU or CPU
            '''
            log_act_probs, value = self.Neural_Network_Architecture(group_of_states)
            probabilities = np.exp(log_act_probs.data.cpu().numpy())

            return probabilities, value.data.numpy()

    def save_network(self, file):
        '''
        The job of this function is the save the Neural Network, in order to continue it's training,
        or in order for the user to play against this current model
        '''
        print("SAVING THE MODEL")

        current_values = self.get_policy_param()  # get model params
        torch.save(current_values, file)

    def parameters(self):
        parameters = self.Neural_Network_Architecture.state_dict()
        return parameters

def learning_rate(optimizer, rate):
    #The learning rate is set to the input values
    for param_group in optimizer.param_groups:
        param_group['lr'] = rate
