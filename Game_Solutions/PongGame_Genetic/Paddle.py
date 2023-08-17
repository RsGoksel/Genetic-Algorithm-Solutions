import numpy as np
import Brain
import random
class Paddle:

    def __init__(self, weights1, weights2):
        
        self.lokasyon = np.array([15,200]) #random_coordinate()
        self.Fitness = 0
        self.hız = 10
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255) )
        
        self.weights1 = weights1
        self.weights2 = weights2
        self.brain = Brain.Brain(self.weights1, self.weights2)
        
        self.commands = {
        0: [self.Rise],
        1: [],
        2: [self.Down]}
    
    def Move(self, top):
        
        max_index = self.brain.predict(self.lokasyon, top).argmax()
        
        for func in self.commands[max_index]:
            func()
    
        self.lokasyon[1] = np.clip(self.lokasyon[1], 100, 550)    
        
    def Rise(self):
        self.lokasyon[1] -= self.hız
    
    def Down(self):
        self.lokasyon[1] += self.hız


