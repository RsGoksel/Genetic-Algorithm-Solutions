import pygame
import random
import time
import numpy as np

import Env

import sys
import traceback
pygame.init()
while True:
    
    try:
        game = Env.Env(Population_Number=50)
        while game.run:
            game.display()
            
        pygame.quit()
        
    except Exception as e:
        pygame.quit()
        break
        
    