import Ball
import Paddle
import Brain

import random
import time

import pygame
import numpy as np

WIDTH = 810 
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
random_coordinate = lambda: np.array([15, random.randint(7, -3+int(HEIGHT/15)) * 15])

class Env:
   
    def __init__(self,Population_Number):
        self.run = True
        self.Ball = Ball.Ball()
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
        
        self.Draw_ball()
        self.Draw_agent()
            
    def reset(self):        
        for i in range(self.Population_Number):
            weights1 = np.random.uniform(-1,1,(3, 7))
            weights2 = np.random.uniform(-1,1,(7, 3))   
            self.Populasyon.append(Paddle.Paddle(weights1, weights2))
            
    def Draw_agent(self):
        
        for eleman in self.Populasyon:
            pygame.draw.rect(screen, (eleman.color[0], eleman.color[1], eleman.color[2]), [eleman.lokasyon[0], eleman.lokasyon[1], 10,30])
            eleman.Move(self.Ball)
            
            if self.Ball.lokasyon[1] >= eleman.lokasyon[1] - 50 and self.Ball.lokasyon[1] < eleman.lokasyon[1] + 30: 
                
                eleman.Fitness += 1
                
                if self.Ball.lokasyon[1] >= eleman.lokasyon[1] and self.Ball.lokasyon[1] < eleman.lokasyon[1] + 10: 
                    eleman.Fitness += 1
                
                if self.Ball.lokasyon[0] < eleman.lokasyon[0]+11:
                    
                    eleman.Fitness += 1
                    self.Ball.flank_x = 1
                    self.Ball.move()  
                    
            else:
                
                self.Died.append(eleman)
                self.Populasyon.remove(eleman)
    
            
            if len(self.Populasyon) < 1: #or self.Ball.lokasyon[0] < eleman.lokasyon[0]:
                self.next_level()
                
        
    def Draw_ball(self):
        
        pygame.draw.rect(screen, (0,120,0), [self.Ball.lokasyon[0], self.Ball.lokasyon[1], 10,10])
        self.Ball.move()
        
    def next_level(self):
        
        self.epoch += 1
        self.Died = sorted(self.Died, key=lambda eleman: eleman.Fitness)

        self.Next_Generation = []
        last_best = int((self.Population_Number - 1) * 0.98)
        self.Next_Generation.extend(self.Died[last_best:])
        self.Besties = self.Died[last_best:]
            
        self.Died.clear()
        self.Ball.reset()
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

                self.Next_Generation.append(Paddle.Paddle(chield_weights_1, chield_weights_2))
            else:
                break
        
        for Member in self.Next_Generation:
            Member.Fitness = 0
            Member.lokasyon = np.array([15,200])
            
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
            print(e)
            self.run = False
            pygame.quit()
    
    def drawGrid(self):
        blockSize = 15 
        for x in range(0, 1200, blockSize):
            for y in range(75, 800, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (25,25,25), rect, 1)