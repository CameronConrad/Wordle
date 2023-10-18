import random

class Logic:
    def __init__(self):
        self.words = []
        self.colors = []
        self.answer = self.get_answer()
        self.current_word = 0
    
    def get_answer(self):
        # Load a random word from the valid-words.csv file
        with open("valid-words.csv", "r") as file:
            words = file.readlines()
        word = random.choice(words)
        return word.strip().upper()
    
    def add_word(self, word):
        self.words.append(word)
        self.current_word = len(self.words) - 1
    
    def check_word(self, index = -1):
        # Return the color for each letter based on the answer
        # If the letter is correct, return green (g)
        # If the letter is incorrect, but in the word, return yellow (y)
        # If the letter is incorrect and not in the word, return gray (n)
        word = self.words[index]
        colors = ["none", "none", "none", "none", "none"]
        for i, letter in enumerate(self.answer):
            if letter == word[i]:
                colors[i] = "green"
            elif letter in word:
                checking_index = word.index(letter)
                if colors[checking_index] == "none":
                    colors[checking_index] = "yellow"
                else:
                    while True:
                        try:
                            checking_index = word.index(letter, checking_index+1)
                            colors[word.index(letter, checking_index)] = "yellow"
                        except ValueError:
                            break
        self.colors.append(colors)
        return colors


def main():
    logic = Logic()
    logic.add_word("WRAHT")
    logic.check_word()
    print(logic.colors)

if __name__ == "__main__":
    main()