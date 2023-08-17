import pygame
import random
import time
import numpy as np

import Agent
import Brain

#Random coordinate for apple and snake head spawn location which restricted to width and height
get_random_apple = lambda: [random.randrange(1,79)*15,random.randrange(6,39)*15]
random_coordinate = lambda: [random.randrange(7,79)*15,random.randrange(6,39)*15]


WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class Env:
   
    def __init__(self,Population_Number):
        
        
        self.run = True
        self.apple = get_random_apple()
        self.Population = []
        self.Population_Number = Population_Number
        self.Died = []
        self.Next_Generation = []
        self.timer = time.time()
        self.epoch = 1
        
        #Creating Agents with their own random initial weights 
        for i in range(self.Population_Number):
            weights1 = np.random.uniform(-1,1,(3, 8))
            weights2 = np.random.uniform(-1,1,(8, 4)) 
            self.Population.append(Agent.Agent(self.apple, weights1, weights2))
        
        
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render("", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (100, 40)
    
    
    def check(self):
        if len(self.Population) < 1:                                                             
            self.crossover()
            self.apple = get_random_apple()

            for agent in self.Population:
                agent.Fitness = 0
                agent.head = random_coordinate()
                agent.distance = np.linalg.norm(np.array(agent.head) - np.array(self.apple))
            
            
    def eat_apple(self):
        
        self.apple = get_random_apple()
        
        for agent in self.Population:
            agent.distance = np.linalg.norm(np.array(agent.head) - np.array(self.apple))
            
            
    def step(self):
        
        pygame.draw.rect(screen, (252,0,0), [self.apple[0],self.apple[1], 15,15])
        
        for agent in self.Population:
            
            for pos in agent.tail:
                pygame.draw.rect(screen, (0,0,120), [pos[0], pos[1], 15,15])
        
            distance = agent.distance
            agent.move(self.apple)
            
            agent.tail.insert(0,list(agent.head))
            agent.tail.pop()
            
            if agent.distance >= distance:  #If snake makes wrong prediction like despite direction to apple, it dies
                
                self.Died.append(agent)
                self.Population.remove(agent)
                self.check()
                
            # +score
            if self.apple == agent.head:
                agent.tail.insert(0,list(agent.head))
                self.eat_apple()
            
            
    def crossover(self):
        self.epoch += 1
        self.Died = sorted(self.Died, key=lambda agent: agent.Fitness)

        self.Next_Generation = []
        last_best = int((self.Population_Number - 1) * 0.95)
        self.Next_Generation.extend(self.Died[last_best:])
        self.Besties = self.Died[last_best:]

        self.Died.clear()
        
        while True:
            if len(self.Next_Generation) < self.Population_Number:
                member_1 = random.choice(self.Besties)
                member_2 = random.choice(self.Besties)

                member_1_weights_1 = member_1.network.weights1
                member_1_weights_2 = member_1.network.weights2

                member_2_weights_1 = member_2.network.weights1
                member_2_weights_2 = member_2.network.weights2

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

                chield_weights_1 = np.array(chield_weights_1).reshape(3,8)
                chield_weights_2 = np.array(chield_weights_2).reshape(8,4)

                self.Next_Generation.append(Agent.Agent(self.apple, chield_weights_1, chield_weights_2))

            else:
                break

        self.Population = self.Next_Generation
        
    
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
            pygame.time.delay(10)          #Optional delay                                                              

        except Exception as e:
            print(e)
            self.run = False
            pygame.quit()
            
    def drawGrid(self):
        blockSize = 15 
        for x in range(0, 1200, blockSize):
            for y in range(75, 800, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (25,25,25), rect, 1)