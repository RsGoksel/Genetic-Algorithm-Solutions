import numpy as np

class Brain:
    def __init__(self,weights1, weights2):
        
        self.weights1 = weights1
        self.weights2 = weights2
        self.Data = np.zeros(3)
        
    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

    def tanh(self,x):
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def swish(self, x):
        return x * self.sigmoid(x)

    def predict(self, lokasyon, top):
        
        #self.Data.fill(0)
        self.Data = np.array([lokasyon[1], top.lokasyon[1], top.lokasyon[0]-lokasyon[0]]) #np.linalg.norm(np.array(lokasyon)-np.array(top.lokasyon))])
        
        self.layer1 = self.swish(np.dot(self.Data, self.weights1))
        self.layer2 = self.softmax(np.dot(self.layer1, self.weights2))
        return self.layer2