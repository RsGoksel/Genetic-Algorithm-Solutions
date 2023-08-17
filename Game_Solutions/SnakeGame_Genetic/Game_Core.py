import Environment
import pygame
import warnings
import traceback
import sys

Number_Of_Agent = 100


while True:
    pygame.init()
    try:    
        game = Environment.Env(Number_Of_Agent)
        
        while game.run:
            game.display()
        pygame.quit()
        
    except Exception as e:
        exc_type, exc_obj, tb = sys.exc_info()
        line_number = tb.tb_lineno
        print("Error!, Hata!", line_number,".th line causing error ")
        traceback.print_exc()
        pygame.quit()
        
    break