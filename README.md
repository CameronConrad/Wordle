# Wordle

This is a Wordle clone. It selects a random word from a csv file of valid Wordle words and has the user attempt to guess the word

## GUI

This program uses the Pygame module for its graphical user interface. 6 rows of tiles with 5 tiles in each row are displayed on the screen. The user types a word, which is displayed in the tiles. The BACKSPACE key can be used to delete letters. When the word has been typed, the user can press RETURN to move to the next line. When this is done, the recently completed row displays colors for each of its tiles. 

## How to play Worldle

The colors of the tiles give hints to the user about what the answer is. Green indicates that the tile's letter is in the right place in the word. Yellow indicates that that letter is in the word, but in the wrong place. And dark gray indicates that the letter is not in the word at all.