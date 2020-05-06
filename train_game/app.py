import pygame


class App:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('My Game')
        self.screen = pygame.display.set_mode((100, 100))
        self.running = False

    def __process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                self.running = False

    def exec(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            self.__process_input()

        pygame.quit()
