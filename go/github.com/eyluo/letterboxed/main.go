package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/eyluo/letterboxed/go/graph"
	"github.com/eyluo/letterboxed/go/util"
)

const (
	smallDict = "../../../../assets/words_easy.txt"
	largeDict = "../../../../assets/words_hard.txt"
	testDict  = "../../../../assets/words_test.txt"

	numSides = 4
	numArgs  = numSides + 2

	usage = "Usage: ./letter_boxed.py <ltter set> <letter set> <letter set> <letter set> <num paths>" +
		"\n\tEach <letter set> is a group of three letters like abc" +
		"\n\tNo letter can be repeated within and across all four sets of letters"
)

func main() {
	if len(os.Args) < numArgs {
		log.Fatalln(usage)
	}

	letters := os.Args[1 : numArgs-1]

	numPaths, err := strconv.Atoi(os.Args[numArgs-1])

	// uppercase all the letters
	for i := range letters {
		letters[i] = strings.ToUpper(letters[i])
	}

	// verify letter set is legal square
	letterSet := util.NewLetterSet(letters)
	if !letterSet.IsLegalSquare() {
		log.Fatalln("Error: illegal square passed in")
	}

	// read dictionary into a list, filtering out illegal words
	file, err := os.Open(smallDict)
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	wordList := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		word := scanner.Text()
		if letterSet.CanMakeWord(word) {
			wordList = append(wordList, word)
		}
	}

	wordSet := util.NewWordSet(wordList)
	wordGraph := graph.New(wordSet)

	fmt.Println(wordGraph.FindPaths(letterSet, numPaths))

	return
}
