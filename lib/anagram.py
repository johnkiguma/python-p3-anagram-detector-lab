# your code goes here!
#messages to complete your work in the lib/ folder.

#You will write a program that, given a word and a list of possible anagramsLinks to an external site., selects the correct one(s).

#Your class, Anagram should take a word on initialization; instances should respond to a match() instance method that takes a list of possible anagrams. It should return all matches in a list. If no matches exist, it should return an empty list.

#In other words, given: 'listen' and ['enlists', 'google', 'inlets', 'banana'] the program should return ['inlets'].

#You can use the following as a reference for how to write your program:

class Anagram:
    example_words = ['enlists', 'google', 'inlets', 'banana']  # List of example words to match against

    def __init__(self, word):
        self.word = word.lower()  # Convert word to lowercase to handle case-insensitive comparisons

    def match(self, words):
        self.word = self.word.lower()
        # Convert all words to lowercase to handle case-insensitive comparisons
        # Return a list of matching words

        return [w for w in words if sorted(self.word) == sorted(w.lower())]

if __name__ == '__main__':
    # Test the Anagram class
    test_word = 'bidet'
    test_anagrams = ['enlists', 'google', 'debit', 'banana']
    anagram_finder = Anagram(test_word)
    matches = anagram_finder.match(test_anagrams)
    print(matches)

