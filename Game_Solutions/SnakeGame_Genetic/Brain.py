import numpy as np

class Brain:
    def __init__(self, weights1, weights2):
        
        self.weights1 = weights1
        self.weights2 = weights2
        
    def softmax(self,x):
        exps = np.exp(x - np.max(x))
        return exps / np.sum(exps)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def swish(self, x):
        return x * self.sigmoid(x)
    
    def predict(self, lokasyon, apple):
        
        self.Data = np.array([lokasyon[0] - apple[0], 
                              lokasyon[1]- apple[1], 
                              np.linalg.norm(np.array(lokasyon) - np.array(apple))])
        
        # Optional.  Normalizing reduces train time. 
        self.Data = self.Data / np.linalg.norm(self.Data)
        
        self.layer1 = self.swish(np.dot(self.Data, self.weights1)) 
        self.layer2 = self.softmax(np.dot(self.layer1, self.weights2)) 
        return self.layer2