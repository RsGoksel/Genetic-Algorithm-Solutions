import NeuralNetwork
import numpy as np
class Bird: # kuş
    def __init__(self,Bird_Image, Bird_Mask, weights1,
                 weights2):
        self.Bird_X = 50
        self.Bird_Y = 50
        self.Gravity = 0.75
        self.acc = 0.075
        self.Bird_Image = Bird_Image
        self.Bird_Mask = Bird_Mask
        self.weight_1 = weights1
        self.weight_2 = weights2

        self.Score = 0

        self.Pipe_Y = 0
        self.Bird_distance_with_pipe = 0

        self.Bird_Network = NeuralNetwork.NeuralNetwork(self.Bird_Y, self.Bird_distance_with_pipe,
                                          self.Pipe_Y, self.weight_1, self.weight_2)

    def Draw_Bird(self,window):
        window.blit(self.Bird_Image,(int(self.Bird_X), int(self.Bird_Y)))

    def Update_NN(self):
        self.Bird_Network.feature_1 = self.Bird_Y
        self.Bird_Network.feature_2 = self.Bird_distance_with_pipe
        self.Bird_Network.feature_3 = self.Pipe_Y

    def Bird_Loop(self):
        if self.Bird_Y < 0:
            return "Died"
        elif self.Bird_Y < 380:
            self.Bird_Y += self.Gravity
            self.Gravity += self.acc
        else:
            return "Died"

        self.Bird_Jump()

    def Bird_Jump(self):
        if self.Bird_Network.predict() < 0.5:
            self.Gravity = -2

