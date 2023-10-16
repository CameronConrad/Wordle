import logic
import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Wordle")
        self.screen_rect = self.screen.get_rect()

        self.word = Word(100, 100)
        self.word.set_word("Hello")
        self.word.sprites()[0].set_fill((255, 0, 0))

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((255, 255, 255))

            self.word.update()
            self.word.draw(self.screen)

            pygame.display.flip()


class Word(pygame.sprite.Group):
    def __init__(self, x, y):
        super().__init__()
        for i in range(0, 5):
            self.add(Tile(50, 50, x+i*60, y))
        self.word = ""

    def update(self):
        for i, letter in enumerate(self.word):
            self.sprites()[i].set_letter(letter)
            self.sprites()[i].update()
    
    def draw(self, screen):
        for sprite in self.sprites():
            sprite.draw(screen)

    def set_word(self, word):
        self.word = word 

class Tile(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.letter = ""
        self.text = pygame.font.SysFont("Arial", 20).render(self.letter, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
    
    def update(self):
        self.letter = self.letter.upper()
        self.text = pygame.font.SysFont("Arial", 20).render(self.letter, True, (0, 0, 0))
        self.text_rect.center = self.rect.center
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text,self.text_rect)
    
    def set_letter(self, letter):
        self.letter = letter
    def set_fill(self,color):
        self.image.fill(color)
        

if __name__ == '__main__':
    game = Game()
    game.run()