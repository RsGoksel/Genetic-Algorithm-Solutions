import numpy as np
import random

class Ball:
    def __init__(self):
        
        self.lokasyon = np.array([200,200])
        self.velocity = 8
        self.flank_x = random.choice([-1, 1])
        self.flank_y = random.choice([-1, 1])
    
    def reset(self):
        self.lokasyon = np.array([200,200])
        self.flank_x = random.choice([-1, 1])
        self.flank_y = random.choice([-1, 1])
    
    def move(self):
        
        self.lokasyon[0] += self.flank_x * self.velocity 
        self.lokasyon[1] += self.flank_y * self.velocity
        
        if self.lokasyon[1] < 100:
            self.flank_y *= -1
            
        if self.lokasyon[1] > 500:
            self.flank_y *= -1
        
        if self.lokasyon[0] > 780:
            self.flank_x *= -1
    