#!/usr/local/bin/python3

import sys
import string

NUM_ARGS = 3
NUM_KEY_LETTERS = 1
NUM_LETTERS = 7
DICT_PATH = './dict.txt'
DICT_PATH = '/usr/share/dict/words'
DICT_PATH = '/Users/eugene/Documents/Personal/word-games/assets/words_easy.txt'
OUT_PATH = './legal_words.txt'
MIN_LENGTH = 4
USAGE = 'usage: python3 %s <letters> <center letter>\n' +\
        'example: python3 abcdefg e'


# returns true if every letter in the word is a legal letter, is at least four
# letters long, and contains the center letter.
def is_legal(key_letter: str, letters: str, word: str) -> bool:
    return len(word) >= 4 and key_letter in word and set(word).issubset(set(letters))


def spelling_bee():
    # ensure sure all letters are provided
    if len(sys.argv) < NUM_ARGS:
        print(USAGE % (sys.argv[0]))
        return

    letters = sys.argv[1]
    key_letter = sys.argv[2]

    # if len(sys.argv) > NUM_ARGS:
    #     DICT_PATH = sys.argv[3]

    # ensure correct number of letters
    if len(letters) != NUM_LETTERS:
        print('error: requires %d letters, but %d were provided' %
              (NUM_LETTERS, len(letters)))
        return

    # ensure no letters are repeated
    if len(letters) != len(set(letters)):
        print('error: repeat letters were provided')
        return

    # ensure all letters are letters
    if not letters.isalpha():
        print('error: a non-letter character was provided')
        return

    # ensure key letter is provided
    if len(key_letter) > NUM_KEY_LETTERS:
        print('error: too many key letters provided')
        return

    # ensure key letter is legal
    if key_letter not in letters:
        print('error: key letter %s does not match any provided letters' %
              (key_letter))
        return

    # go through dictionary and filter out legal words
    with open(DICT_PATH, 'r') as r, open(OUT_PATH, 'w') as w:
        words = r.readlines()
        legal_words = list()
        count = 0
        for word in words:
            word = word.strip().lower()
            if is_legal(key_letter, letters, word):
                count += 1
                legal_words.append(word)

        legal_words.sort(key=len, reverse=True)

        for word in legal_words:
            w.write('%s\n' % (word))

    print('found %d words written to %s' % (count, OUT_PATH))


if __name__ == '__main__':
    spelling_bee()
