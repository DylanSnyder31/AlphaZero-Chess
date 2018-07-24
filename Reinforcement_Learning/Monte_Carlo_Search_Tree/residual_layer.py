'''
This is the residual layer to the NN, the structure is:

Input -> 256 convolutional filters (3x3) -> Batch Normalization -> Rectifier non-linearity ->
256 convolutional filters (3x3) -> Batch Normalization -> Skip Connection -> Rectifier non-linearity
'''

class residual():

    def __init__(self):
        pass

    #Call the convolutional_layer (full)

    #256 Convolutional Layers (3x3)

    #Batch Normalization

    #Skip Connection

    #rectifier non linearity

    self.conv1 = nn.Conv2d(channel, channel, kernel_size=3, padding=1)
    self.conv1_bn = nn.BatchNorm2d(channel)
    self.conv1_relu = nn.ReLU(inplace=True)
    
    self.conv2 = nn.Conv2d(channel, channel, kernel_size=3, padding=1)
    self.conv2_bn = nn.BatchNorm2d(channel)
    # forward엔 여기에 skip connection 추가 필요
    self.conv2_relu = nn.ReLU(inplace=True)
