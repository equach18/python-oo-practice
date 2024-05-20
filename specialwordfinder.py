"""Special Word Finder: finds random words from a dictionary, excluding blank lines and comments."""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Finds a word in the file, excluding blanks and comments
    >>> special_wrd = SpecialWordFinder("specialwords.txt")
    4 words read

    >>> isinstance(special_wrd, SpecialWordFinder)
    True

    >>> special_wrd.random() in special_wrd.word_list
    True

    >>> special_wrd.random() in ["kale", "parsenips", "apple", "mango"] 
    True
    """
    def parseWords(self):
        """Parses the file into a list of words, excluding the blank lines and comments"""
        return [word.strip() for word in self.file if not word.startswith("#") and word.strip()]