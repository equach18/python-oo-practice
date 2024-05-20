"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Finds a word in the file
    >>> wrd = WordFinder("fewwords.txt")
    5 words read

    >>> isinstance(wrd, WordFinder)
    True

    >>> wrd.random() in wrd.word_list
    True

    >>> wrd.random() in ["car", "house", "dog", "tree", "cat"]
    True
    """

    def __init__(self, file):
        """Opens the file and prints out the number of items read"""
        self.file = open(file)
        self.word_list = self.parseWords()
        print(f"{len(self.word_list)} words read")
    
    def parseWords(self):
        """Parses the given file into a list of words"""
        return [word.strip() for word in self.file]
    
    def random(self):
        """Returns a random word from the list of words"""
        return choice(self.word_list)
