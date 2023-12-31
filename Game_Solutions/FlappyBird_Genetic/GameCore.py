import pygame
import Pipe
import random
import numpy as np
import Bird
class GameCore:
    def __init__(self, Population_Number = 1):
        self.window_height = 288
        self.window_width = 512
        self.window = pygame.display.set_mode((self.window_height,self.window_width))
        self.Clock = pygame.time.Clock()
        self.GameSpeed = 2
    

        self.BackGround = pygame.image.load("assets/background.png").convert()

        self.Base = pygame.image.load("assets/base.png").convert()

        self.Pipe_Image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.Pipe_Number = 0


        self.Bird_Image = pygame.image.load("assets/bird.png").convert_alpha()
        self.Bird_Mask = pygame.mask.from_surface(self.Bird_Image)

        self.Font_T = pygame.font.SysFont("Arial", 40)


        self.Pipe_List = [
            Pipe.Pipe(300, random.randint(150, 340), 0, self.Pipe_Image),
            Pipe.Pipe(460, random.randint(150, 340), 1, self.Pipe_Image),
            Pipe.Pipe(620, random.randint(150, 340), 2, self.Pipe_Image),
            Pipe.Pipe(780, random.randint(150, 340), 3, self.Pipe_Image)
        ]
        self.Pipe_id = 4

        self.Population = []
        self.Next_Generation = []
        self.Population_Number = Population_Number
        self.Died_Bird = []
        self.Generation_Timer = 0

        for i in range(self.Population_Number):
            weights1, weights2 = self.create_weights()
            self.Population.append(Bird.Bird(self.Bird_Image, self.Bird_Mask, weights1, weights2))

    def create_weights(self):
        weights1 = np.random.uniform(-1,1,(3,7))
        weights2 = np.random.uniform(-1,1,(7,1))
        return weights1, weights2

    def MaskCollision(self, Masked_Image1, Image1_X, Image1_Y, Masked_Image2, Image2_X, Image2_Y):
        offset = (round(Image2_X - Image1_X), round(Image2_Y - Image1_Y))
        result = Masked_Image1.overlap(Masked_Image2, offset)
        return result

    def Draw(self):

        self.window.blit(self.BackGround,(0,0))
        self.window.blit(self.Base,(0, 400))

        for pipe in self.Pipe_List:
            pipe.Draw_Pipe(self.window)

        for Bird in self.Population:
            Bird.Draw_Bird(self.window)

        self.Clock.tick(60)
        pygame.display.update()

    def crossover(self):
        self.Died_Bird = sorted(self.Died_Bird, key=lambda Bird: Bird.Score)

        self.Next_Generation = []
        last_best = int((self.Population_Number - 1) * 0.98)
        self.Next_Generation.extend(self.Died_Bird[last_best:])
        self.Besties = self.Died_Bird[last_best:]
        for Member in self.Next_Generation:
            Member.Bird_X = 50
            Member.Bird_Y = 50
            Member.Score = 0
            Member.Gravity = 0.75

        self.Died_Bird.clear()

        while True:
            if len(self.Next_Generation) < self.Population_Number:

                member_1 = random.choice(self.Besties)
                member_2 = random.choice(self.Besties)

                member_1_weights_1 = member_1.Bird_Network.weights1
                member_1_weights_2 = member_1.Bird_Network.weights2

                member_2_weights_1 = member_2.Bird_Network.weights1
                member_2_weights_2 = member_2.Bird_Network.weights2

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
                chield_weights_2 = np.array(chield_weights_2).reshape(7,1)

                self.Next_Generation.append(Bird.Bird(self.Bird_Image, self.Bird_Mask,
                                                 chield_weights_1, chield_weights_2))


            else:
                break

        self.Population = self.Next_Generation


    def restart_game(self):
        self.Pipe_List = [
            Pipe.Pipe(300, random.randint(100, 380), 0, self.Pipe_Image),
            Pipe.Pipe(460, random.randint(100, 380), 1, self.Pipe_Image),
            Pipe.Pipe(620, random.randint(100, 380), 2, self.Pipe_Image),
            Pipe.Pipe(780, random.randint(100, 380), 3, self.Pipe_Image)
        ]

        self.crossover()

    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Close"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Close"

        self.FPS = str(int(self.Clock.get_fps()))
        pygame.display.set_caption(f"Fps : {self.FPS}")

        for pipe in self.Pipe_List:
            if pipe.Pipe_X == -52:
                pipe.Pipe_X = 588
                pipe.Pipe_Lower_Y = random.randint(220, 340)
                pipe.Pipe_Upper_Y = pipe.Pipe_Lower_Y - 420
                pipe.Pipe_id = self.Pipe_id
                self.Pipe_id += 1

            pipe.Move_Pipe(self.GameSpeed)

            for Member in self.Population:
                if Member.Score == pipe.Pipe_id:
                    Member.Bird_distance_with_pipe = pipe.Pipe_X - Member.Bird_X
                    Member.Pipe_Y = pipe.Pipe_Lower_Y
                    Member.Update_NN()

                collision_lower = self.MaskCollision(Member.Bird_Mask, Member.Bird_X, Member.Bird_Y,
                                                     pipe.Pipe_Lower_Mask,pipe.Pipe_X,pipe.Pipe_Lower_Y)
                collision_upper = self.MaskCollision(Member.Bird_Mask, Member.Bird_X, Member.Bird_Y,
                                                     pipe.Pipe_Upper_Mask,pipe.Pipe_X,pipe.Pipe_Upper_Y)

                if collision_lower != None or collision_upper != None:
                    self.Died_Bird.append(Member)
                    self.Population.remove(Member)

                if Member.Bird_X + 16 == pipe.Pipe_X:
                    Member.Score += 1

        for Member in self.Population:
            if Member.Bird_Loop() == "Died":
                self.Died_Bird.append(Member)
                self.Population.remove(Member)

        if len(self.Population) == 0:
            self.restart_game()
            self.Pipe_id = 4
            self.Generation_Timer += 1

        self.Draw()