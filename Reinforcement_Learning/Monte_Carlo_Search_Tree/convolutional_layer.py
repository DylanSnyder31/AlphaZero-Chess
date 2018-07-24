
'''
This is the convolutional layer to the NN, the structure is:

Input -> 256 convolutional filters (3x3) -> Batch Normalization -> Rectifier non-linearity
'''

class convolution():

    def __init__(self, board_height, board_width):

        pass

    def layer_convolutional(self):
        self.conv1 = nn.Conv2d(5, channel, kernel_size=3, padding=1)

    def batch_normalization(self):
        self.conv_bn = nn.BatchNorm2d(channel)

    def rectifier_non_linearity(self):
        self.conv_relu = nn.ReLU(inplace=True)
