import pygame

class Pipe:
    def __init__(self, Pipe_X, Pipe_Y, Pipe_id,Pipe_Image):
        self.Pipe_X = Pipe_X
        self.Pipe_Lower_Y = Pipe_Y
        self.Pipe_Upper_Y = self.Pipe_Lower_Y - 420
        self.Pipe_id = Pipe_id
        self.Pipe_Lower_Image = Pipe_Image
        self.Pipe_Upper_Image = pygame.transform.flip(self.Pipe_Lower_Image, False, True)

        self.Pipe_Lower_Mask = pygame.mask.from_surface(self.Pipe_Lower_Image)
        self.Pipe_Upper_Mask = pygame.mask.from_surface(self.Pipe_Upper_Image)

    def Draw_Pipe(self,window):
        window.blit(self.Pipe_Lower_Image,(self.Pipe_X, self.Pipe_Lower_Y))
        window.blit(self.Pipe_Upper_Image,(self.Pipe_X, self.Pipe_Upper_Y))

    def Move_Pipe(self, GameSpeed):
        self.Pipe_X -= 1 * GameSpeed
