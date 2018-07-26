from Reinforcement_Learning.Monte_Carlo_Search_Tree.convolutional_layer import convolution
import torch
import torch.nn as nn
'''
This this the policy head, the structure is:

Input -> 2 Convolutional filters (1x1) -> Batch Normalization -> Rectifier Non-linearity ->
Fully Connected Layer (move logit probabilities)
'''

class policy():

    def main(self, channel):
        self.convo = convolutional()

        self.policy_head = nn.Conv2d(channel, 2, kernel_size=1)

        self.policy_head = self.convo.batch_normalization(self.policy_head)
        self.policy_head = self.convo.rectifier_non_linearity(self.policy_head)

        self.policy_head = nn.Linear(18, 9)
        self.policy_head = nn.Softmax(dim=1)

        return self.policy_head
