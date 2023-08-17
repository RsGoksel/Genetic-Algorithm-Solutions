import pygame
import random
import time
import numpy as np
import warnings
import traceback
import sys
warnings.filterwarnings('ignore')

WIDTH = 810
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
random_coordinate = lambda: np.array([15, random.randint(7, -3+int(HEIGHT/15)) * 15])
            
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

    def predict(self, location, Ball):
        
        #self.Data.fill(0)
        self.Data = np.array([location[1], Ball.location[1], Ball.location[0]-location[0]]) #np.linalg.norm(np.array(location)-np.array(Ball.location))])
        
        self.layer1 = self.swish(np.dot(self.Data, self.weights1))
        self.layer2 = self.softmax(np.dot(self.layer1, self.weights2))
        return self.layer2
    
class Ball:
    def __init__(self):
        
        self.location = np.array([200,200])
        self.velocity = 8
        self.flankx = random.choice([-1, 1])
        self.flanky = random.choice([-1, 1])
    
    def res(self):
        self.location = np.array([200,200])
        self.flankx = random.choice([-1, 1])
        self.flanky = random.choice([-1, 1])
    
    def move(self):
        
        self.location[0] += self.flankx * self.velocity 
        self.location[1] += self.flanky * self.velocity 
        
        if self.location[1] < 100:
            self.flanky *= -1
            
        if self.location[1] > 500:
            self.flanky *= -1
        
        if self.location[0] > 780:
            self.flankx *= -1
    
class Paddle:

    def __init__(self, weights1, weights2):
        
        self.location = np.array([15,200]) #random_coordinate()
        self.Fitness = 0
        self.velocity = 10
        
        self.weights1 = weights1
        self.weights2 = weights2
        self.brain = Brain(self.weights1, self.weights2)
        
        self.commands = {
        0: [self.rise],
        1: [],
        2: [self.down]}
    
    def kaptır(self, Ball):
        
        max_index = self.brain.predict(self.location, Ball).argmax()
        
        for func in self.commands[max_index]:
            func()
    
        self.location[1] = np.clip(self.location[1], 100, 550)    
        
    def rise(self):
        self.location[1] -= self.velocity
    
    def down(self):
        self.location[1] += self.velocity
    
    
class Env:
   
    def __init__(self,Population_Number):
        self.run = True
        self.Ball = Ball()
        self.Populasyon = []
        self.Population_Number = Population_Number
        self.Died = []
        self.Next_Generation = []
        self.epoch = 1
        
        self.reset()
        self.timer = time.time()
        
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render("", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (100, 40)
        
    def step(self):
        
        self.draw_Ball()
        self.draw_agent()
            
            
    def reset(self):        
        for i in range(self.Population_Number):
            weights1 = np.random.uniform(-1,1,(3, 7))
            weights2 = np.random.uniform(-1,1,(7, 3))   
            self.Populasyon.append(Paddle(weights1, weights2))
            
    def draw_agent(self):
        
        for agent in self.Populasyon:
            pygame.draw.rect(screen, (0,0,120), [agent.location[0], agent.location[1], 10,30])
            agent.kaptır(self.Ball)
            
            if self.Ball.location[1] >= agent.location[1] - 50 and self.Ball.location[1] < agent.location[1] + 30: 
                
                agent.Fitness += 1
                
                if self.Ball.location[1] >= agent.location[1] and self.Ball.location[1] < agent.location[1] + 10: 
                    agent.Fitness += 1
                
                if self.Ball.location[0] < agent.location[0]+11:
                    
                    agent.Fitness += 1
                    self.Ball.flankx = 1
                    self.Ball.move()  
                    
            else:
                
                self.Died.append(agent)
                self.Populasyon.remove(agent)
    
            
            if len(self.Populasyon) < 1: #or self.Ball.location[0] < agent.location[0]:
                self.next_level()
                
        
    def draw_Ball(self):
        
        pygame.draw.rect(screen, (0,120,0), [self.Ball.location[0], self.Ball.location[1], 10,10])
        self.Ball.move()
        
    def next_level(self):
        
        self.epoch += 1
        self.Died = sorted(self.Died, key=lambda agent: agent.Fitness)

        self.Next_Generation = []
        last_best = int((self.Population_Number - 1) * 0.98)
        self.Next_Generation.extend(self.Died[last_best:])
        self.Besties = self.Died[last_best:]
            
        self.Died.clear()
        self.Ball.res()
        self.timer = time.time()
        while True:
            if len(self.Next_Generation) < self.Population_Number:
                member_1 = random.choice(self.Besties)
                member_2 = random.choice(self.Besties)

                member_1_weights_1 = member_1.brain.weights1
                member_1_weights_2 = member_1.brain.weights2

                member_2_weights_1 = member_2.brain.weights1
                member_2_weights_2 = member_2.brain.weights2

                chield_weights_1 = []
                chield_weights_2 = []

                for a,b in zip(member_1_weights_1, member_2_weights_1):
                    for c,d in zip(a,b):
                        prob = random.random()
                        if prob < 0.47:
                            chield_weights_1.append(c)
                        elif prob < 0.94:
                            chield_weights_1.append(d)
                        else:
                            chield_weights_1.append(random.uniform(-1, 1))

                for e,f in zip(member_1_weights_2, member_2_weights_2): #7/1
                    for g,h in zip(e,f):
                        prob = random.random()
                        if prob < 0.47:
                            chield_weights_2.append(g)
                        elif prob < 0.94:
                            chield_weights_2.append(h)
                        else:
                            chield_weights_2.append(random.uniform(-1, 1))

                chield_weights_1 = np.array(chield_weights_1).reshape(3,7)
                chield_weights_2 = np.array(chield_weights_2).reshape(7,3)

                self.Next_Generation.append(Paddle(chield_weights_1, chield_weights_2))
            else:
                break
        
        for Member in self.Next_Generation:
            Member.Fitness = 0
            Member.location = np.array([15,200])
            
        self.Populasyon = self.Next_Generation
        
        
    def display(self):
        
        try:
            screen.fill((0,0,0))
            self.drawGrid()
            self.step()

            self.text_surface = self.font.render("Generation / Nesil: "+str(self.epoch), True, (255, 255, 255))
            screen.blit(self.text_surface, self.text_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
            clock.tick(60)

        except Exception as e:
            exc_type, exc_obj, tb = sys.exc_info()
            line_number = tb.tb_lineno
            print("Hata!", line_number,". Satırda hata meydana geldi")
            traceback.print_exc()
            self.run = False
            pygame.quit()
    
    def drawGrid(self):
        blockSize = 15 
        for x in range(0, 1200, blockSize):
            for y in range(75, 800, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (25,25,25), rect, 1)
                
while True:
    pygame.init()
    try:
        game = Env(Population_Number=50)
        while game.run:
            game.display()
        pygame.quit()
    except Exception as e:
        exc_type, exc_obj, tb = sys.exc_info()
        print("Exception occurred on line:", line_number)
        traceback.print_exc()
    break
    