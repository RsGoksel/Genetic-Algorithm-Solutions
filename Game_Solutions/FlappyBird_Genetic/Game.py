import pygame
import random
import time
import numpy as np

import Bird
import NeuralNetwork
import Pipe
import GameCore

pygame.init()

Population_Number = 500
Game = GameCore.GameCore(Population_Number)

while True:
    GameStatus = Game.GameLoop()
    if GameStatus == "Close":
        break
    #MechSons = 
pygame.quit()