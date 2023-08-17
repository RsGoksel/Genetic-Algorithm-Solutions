import random
import numpy as np
import Environment
import Brain

class Agent:

    def __init__(self, apple, weights1, weights2):
        
        x = random.randint(30, Environment.WIDTH-50)
        x -= x % 15 or 1
        #x = (lambda num: num - num % 15 or 1)(random.randint(100, 1000))
        
        y = random.randint(100, Environment.HEIGHT-50)
        y -= y % 15 or 1
        
        self.head = [x,y]
        self.tail = [[x+15,y],[x+30,y],[x+45,y]]
        self.distance = np.linalg.norm(np.array(self.head) - np.array(apple))   # distance = difference. This will take euclid distance of snake head and apple
        self.Fitness = 0
        
        self.network = Brain.Brain(weights1, weights2)
      
        self.commands = {
        0: [self.right],
        1: [self.down],
        2: [self.left],
        3: [self.up],
        }
        
    def move(self, apple):
        
        karar = self.network.predict(self.head, apple).argmax()   #Index of neural network prediction. Which mentioned at self.coomands just upside
        
        for func in self.commands[karar]:
            func()
        
        # Clipping the coordinates for keep Snakes head in game screen
        self.head[0] = np.clip(self.head[0], 0, Environment.WIDTH-15)
        self.head[1] = np.clip(self.head[1], 75, Environment.HEIGHT-15)
        
        # Update current distance
        self.distance = np.linalg.norm(np.array(self.head) - np.array(apple))
        
    # Left command
    def left(self):
        self.head[0] -= 15
    
    #Right command
    def right(self):
        self.head[0] += 15
        
    # Go to top command
    def up(self):
        self.head[1] -= 15
        
    # Go to bottom command
    def down(self):
        self.head[1] += 15