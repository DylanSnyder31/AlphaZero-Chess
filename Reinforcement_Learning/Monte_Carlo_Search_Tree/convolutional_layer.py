import torch
import torch.nn as nn

'''
This is the convolutional layer to the NN, the structure is:

Input -> 256 convolutional filters (3x3) -> Batch Normalization -> Rectifier non-linearity
'''

class convolution():

    def __init__(self, board_height, board_width):

        pass

    def layer_convolutional(self, channel):
        self.conv1 = nn.Conv2d(5, channel, kernel_size=3, padding=1)
        return self.conv1

    def batch_normalization(self, channel):
        self.conv_bn = nn.BatchNorm2d(channel)
        return self.conv_bn

    def rectifier_non_linearity(self, channel):
        self.conv_relu = nn.ReLU(inplace=True)
        return self.conv_relu

    def main(self, state):
        self.conv1 = self.layer_convolutional(state)
        self.conv_bn = self.batch_normalization(self.conv1)
        self.conv_relu = self.rectifier_non_linearity(self.conv_bn)

        return self.conv_relu
