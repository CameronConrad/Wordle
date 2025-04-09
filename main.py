import logic
import pygame
import sys
from colors import color_dict


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Wordle")
        self.screen_rect = self.screen.get_rect()

        self.logic = logic.Logic()

        self.words = []
        for i in range(0, 6):
            self.words.append(Word(50, 50 + i*60))

        self.active_word_index = 0
        self.active_word = ""

        self.clock = pygame.time.Clock()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and len(self.active_word) < 5:
                    self.active_word += event.unicode.upper()
                elif event.key == pygame.K_RETURN and len(self.active_word) == 5:
                    self.logic.add_word(self.active_word)
                    self.set_word(self.active_word, self.active_word_index)
                    self.update_colors()
                    self.active_word_index += 1
                    self.active_word = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.active_word = self.active_word[:-1]

    def run(self):
        while True:
            self.check_events()

            self.screen.fill((255, 255, 255))

            self.set_word(self.active_word, self.active_word_index)

            for word in self.words:
                word.update()
                word.draw(self.screen)

            pygame.display.flip()

    def update_colors(self):
        for i, word in enumerate(self.logic.words):
            self.set_word(word, i)
            results = []
            for color in self.logic.check_word(i):
                results.append(color_dict[color])
            self.set_colors(results, i)

    def set_word(self, word, index):
        try:
            self.words[index].set_word(word)
        except IndexError:
            print(f"The word was {self.logic.answer}")

    def set_colors(self, colors: list, index):
        self.words[index].set_colors(colors)


class Word(pygame.sprite.Group):
    def __init__(self, x, y):
        super().__init__()
        for i in range(0, 5):
            self.add(Tile(50, 50, x+i*60, y))
        self.word = ""

    def update(self):
        last_index = 0
        for i, letter in enumerate(self.word):
            self.sprites()[i].set_letter(letter)
            self.sprites()[i].update()
            last_index += 1
        for i in range(last_index, 5):
            self.sprites()[i].set_letter("")
            self.sprites()[i].update()

    def draw(self, screen):
        for sprite in self.sprites():
            sprite.draw(screen)

    def set_word(self, word):
        self.word = word

    def set_colors(self, colors: list):
        for i, color in enumerate(colors):
            self.sprites()[i].set_fill(color)


class Tile(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.letter = ""
        self.text = pygame.font.SysFont("Arial", 20).render(
            self.letter, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()

    def update(self):
        self.letter = self.letter.upper()
        self.text = pygame.font.SysFont("Arial", 20).render(
            self.letter, True, (0, 0, 0))
        self.text_rect.center = (self.rect.centerx-5, self.rect.centery)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def set_letter(self, letter):
        self.letter = letter

    def set_fill(self, color):
        self.image.fill(color)


if __name__ == '__main__':
    game = Game()
    game.run()
