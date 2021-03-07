#!/usr/local/bin/python3

import sys
import word_gen
import word_graph

NUM_ARGS = 5
USAGE = 'Usage: ./letter_boxed.py <ltter set> <letter set> <letter set> <letter set>' +\
        '\n\tEach <letter set> is a group of three letters like abc' +\
        '\n\tNo letter can be repeated within and across all four sets of letters'
MAX_DEPTH = 3


def main():
    if len(sys.argv) < NUM_ARGS:
        print(USAGE)
        return 1

    sides = sys.argv[1:NUM_ARGS]

    # capitalize everything if not already capitalized
    sides = list(map(lambda side: list(map(lambda c: c.upper(), side)), sides))

    # get all the legal words
    word_set = word_gen.word_gen(sides)

    # generate the word graph
    graph = word_graph.Graph(word_set)

    # traverse the graph
    print(graph.find_paths(sides, max_depth=MAX_DEPTH, max_results=-1))


if __name__ == '__main__':
    main()
