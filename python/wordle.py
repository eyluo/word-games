'''Solves wordle puzzle.'''

from sys import argv
from enum import Enum
from random import choice
from wordle_words import answers, dictionary


DEFAULT_NUM_GUESSES = 6


class LetterStatus(Enum):
    GREEN = 1   # Letter is in the correct place
    YELLOW = 2  # Letter is in the word
    BLACK = 3   # Letter is not in the word

    def __str__(self):
        if self.name == 'BLACK':
            return '⬛️'
        if self.name == 'YELLOW':
            return '🟨'
        if self.name == 'GREEN':
            return '🟩'


class Solver():
    '''Solves wordle.'''

    def __init__(self, answer, max_num_guesses=DEFAULT_NUM_GUESSES):
        '''Initializes solver.'''
        self.answer = answer
        self.max_num_guesses = max_num_guesses

        self.dictionary = answers[0] + dictionary[0]

        self.guesses = []

    def solve(self):
        '''Solves wordle.'''
        def solve_helper(guess_number):
            def select_guess():
                return choice(self.dictionary).lower().strip()

            def compare_words(answer, guess):
                result = []
                for i, char in enumerate(guess):
                    if answer[i] == char:
                        result.append(LetterStatus.GREEN)
                    elif char in answer:
                        result.append(LetterStatus.YELLOW)
                    else:
                        result.append(LetterStatus.BLACK)
                return result

            if guess_number == self.max_num_guesses:
                return False

            guess = select_guess()
            self.guesses.append(guess)

            # If you interface this with wordle, then you can run this program
            # without providing an answer.
            letter_statuses = compare_words(self.answer, guess)
            print(
                f'{guess}: {"".join(map(str, letter_statuses))}')

            if guess == self.answer:
                return True

            # Checks a word against a letter status and returns True if the word
            # satisfies the criteria. Otherwise, returns False.
            def filter_words(word):
                if word == guess:
                    return False
                for i, status in enumerate(letter_statuses):
                    if status == LetterStatus.GREEN:
                        if word[i] != guess[i]:
                            return False
                    elif status == LetterStatus.YELLOW:
                        if word[i] == guess[i] or guess[i] not in word:
                            return False
                    elif status == LetterStatus.BLACK:
                        if guess[i] in word:
                            return False
                return True
            self.dictionary = list(filter(filter_words, self.dictionary))

            return solve_helper(guess_number+1)

        if self.answer not in self.dictionary:
            print(f'{self.answer} is not in the dictionary. Cannot solve')
            return

        guessed = solve_helper(0)

        if guessed:
            print(f'Solved wordle for {self.answer} in {len(self.guesses)} guess' +
                  'es' if len(self.guesses) != 1 else '')
        else:
            print(f'Unable to solve wordle for {self.answer}')
        print(self.guesses)


def main():
    '''Main function.'''
    if len(argv) < 2:
        print('Must specify word to guess')
        return

    answer = argv[1]

    wordle = Solver(answer.lower())
    wordle.solve()

    return


if __name__ == '__main__':
    main()
