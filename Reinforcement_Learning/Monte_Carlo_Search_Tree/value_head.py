from Reinforcement_Learning.Monte_Carlo_Search_Tree.convolutional_layer import convolution
import torch
import torch.nn as nn
'''
This is the value head, the structure is:

Input -> 1 Convolutional Layer (1x1) -> Batch Normalization -> Rectifier non-linearity ->
fully connected layer (hidden layer size 256) -> Rectifier non-rectifier non-linearity ->
Fully Connected Layer (to Scalar) -> tahn non-linearity
'''

class value():

    def __init__(self):
        self.convo = convolutional()

    def main(self):
        self.value_head = nn.Conv2d(channel, 1, kernel_size=1)

        self.value_head = self.convo.batch_normalization()

        self.value_head = self.convo.rectifier_non_linearity()

        self.value_head = nn.Linear(9, channel)

        self.value_head = self.convo.rectifier_non_linearity()

        self.value_head = nn.Linear(channel, 1)

        self.value_head = nn.Tanh()

        return self.value_head
