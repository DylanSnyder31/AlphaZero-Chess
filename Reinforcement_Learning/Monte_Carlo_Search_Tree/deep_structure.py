from Reinforcement_Learning.Monte_Carlo_Search_Tree.convolutional_layer import convolution
from Reinforcement_Learning.Monte_Carlo_Search_Tree.residual_layer import residual

from Reinforcement_Learning.Monte_Carlo_Search_Tree.value_head import value
from Reinforcement_Learning.Monte_Carlo_Search_Tree.policy_head import policy

'''
This is the structure of the Deep Neural Network:

Input -> convolutional layer -> 40 residual layers -> Value amd policy heads
'''

class architecture():

    def __init__(self, state):
        self.state = state
        self.convolution = convolution()
        self.residual = residual()
        self.head_value = value()
        self.head_policy = policy()

    def layer_convolutional(self):
        self.finished_convolutional = self.convolution.main(self.state)
        return self.finished_convolutional

    def residual_layers(self):
        self.RESIDUAL = self.finished_convolutional
        for i in range(40):
            self.RESIDUAL = self.residual.main(self.RESIDUAL)
        return self.RESIDUAL

    def both_heads(self):
        V_val = self.head_value.main(self.finished_residual)
        P_val = self.head_policy.main(self.finished_residual)
        return p_val, V_val

    def main(self):
        self.finished_convolutional = self.layer_convolutional()
        self.finished_residual = self.residual_layers()
        self.P_value, self.V_value = self.both_heads()
