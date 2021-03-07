from typing import List, Set, Dict
import csv

EASY_MODE = 0
HARD_MODE = 1
TEST_MODE = 2

LETTERS_PER_SIDE = 3
NUM_SIDES = 4
LETTER_COUNT = LETTERS_PER_SIDE * NUM_SIDES


def word_gen(sides: List[str], mode=EASY_MODE) -> Set[str]:
    # given a list of letters on each side of the square, return a list of all
    # legal words in the dictionary file

    # -----------------
    # utility functions
    # -----------------

    def no_repeat_letters(sides: List[str]) -> (bool, Set[str]):
        letter_set = set()
        for side in sides:
            for char in side:
                letter_set.add(char)
        if len(letter_set) == LETTER_COUNT:
            return True, letter_set
        else:
            return False, None

    def str_to_letter_set(s: str) -> Set[str]:
        letter_set = set()
        for c in s:
            letter_set.add(c)
        return letter_set

    def build_reverse_letter_index(sides: List[str]) -> Dict[str, int]:
        reverse_index = dict()
        for i in range(len(sides)):
            for c in sides[i]:
                reverse_index[c] = i
        return reverse_index

    # ---------------------
    # end utility functions
    # ---------------------

    # arg validation
    if len(sides) != NUM_SIDES or len(sides[0]) != LETTERS_PER_SIDE:
        print('Error: illegal argument passed in. Make sure you only passed in 4 sides with 3 letters apiece.')
        return None

    legal_letters, legal_letter_set = no_repeat_letters(sides)

    if not legal_letters:
        print('Error: illegal argument passed in. Make sure no letters repeat.')
        return None

    letter_reverse_index = build_reverse_letter_index(sides)

    def is_legal_word(word: str) -> bool:
        # we don't need to check word length because the dictionaries are
        # already filtered for words of length 3 or greater
        word_letter_set = str_to_letter_set(word)
        if not word_letter_set.issubset(legal_letter_set):
            return False

        # consecutive letters cannot come from the same side of the square
        prev_letter_index = -1
        for c in word:
            curr_letter_index = letter_reverse_index[c]
            if letter_reverse_index[c] == prev_letter_index:
                return False
            prev_letter_index = curr_letter_index

        return True

    # use the correct word set if needed
    if mode == EASY_MODE:
        word_file = '../assets/words_easy.txt'
    elif mode == HARD_MODE:
        word_file = '../assets/words_hard.txt'
    elif mode == TEST_MODE:
        word_file = '../assets/words_test.txt'
    else:
        print('Error: illegal mode passed in')
        return None

    word_set = set()
    with open(word_file, 'r') as r:
        reader = csv.reader(r)

        for line in reader:
            word = ''.join(line).strip()

            if is_legal_word(word):
                word_set.add(''.join(line).strip())

    return word_set
