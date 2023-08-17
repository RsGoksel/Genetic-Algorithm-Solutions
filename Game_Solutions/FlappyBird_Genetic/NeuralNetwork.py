import numpy as np
class NeuralNetwork:
    def __init__(self,feature_1, feature_2, feature_3, weights1, weights2):
        self.feature_1 = feature_1
        self.feature_2 = feature_2
        self.feature_3 = feature_3
        self.weights1 = weights1
        self.weights2 = weights2

    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def predict(self):
        self.Data = np.array([self.feature_1, self.feature_2, self.feature_3]) # 1,3
        self.layer1 = self.sigmoid(np.dot(self.Data, self.weights1)) # 1,3 - 3,7 = 1,7
        self.layer2 = self.sigmoid(np.dot(self.layer1, self.weights2)) # matris çarpımı
        return self.layer2
