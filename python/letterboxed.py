#!/usr/local/bin/python3

import sys
import word_gen
import word_graph

NUM_ARGS = 5
NUM_OPTIONAL_ARGS = 2
USAGE = 'Usage: ./letter_boxed.py <letter set> <letter set> <letter set> <letter set> <optional depth> <optional num results>' +\
        '\n\tEach <letter set> is a group of three letters like abc' +\
        '\n\tNo letter can be repeated within and across all four sets of letters'
EXCEPTION_STR = 'Please specify integer values for optional arguments'
DEFAULT_DEPTH = 2
DEFAULT_NUM_RESULTS = 5


def main():
    if len(sys.argv) < NUM_ARGS:
        print(USAGE)
        return 1

    sides = sys.argv[1:NUM_ARGS]

    if len(sys.argv) >= NUM_ARGS + NUM_OPTIONAL_ARGS:
        try:
            depth = int(sys.argv[NUM_ARGS])
            num_results = int(sys.argv[NUM_ARGS+1])
        except:
            print(EXCEPTION_STR)
            return 1
    else:
        depth = DEFAULT_DEPTH
        num_results = DEFAULT_NUM_RESULTS

        # capitalize everything if not already capitalized
    sides = list(map(lambda side: list(map(lambda c: c.upper(), side)), sides))

    # get all the legal words
    word_set = word_gen.word_gen(sides)

    # generate the word graph
    graph = word_graph.Graph(word_set)

    # traverse the graph
    print(graph.find_paths(sides, max_depth=depth, max_results=num_results))

    return 0


if __name__ == '__main__':
    main()
