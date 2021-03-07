package graph

import (
	"github.com/eyluo/letterboxed/go/util"
)

const (
	maxDepth        = 3
	defaultMaxPaths = 3
)

type Graph struct {
	adjList map[string]util.WordSet
}

func New(wordWordSet util.WordSet) *Graph {
	res := &Graph{}

	res.adjList = make(map[string]util.WordSet)
	for rootWord := range wordWordSet {
		res.adjList[rootWord] = util.NewWordSet(nil)
		for outgoingWord := range wordWordSet {
			if rootWord != outgoingWord && rootWord[len(rootWord)-1] == outgoingWord[0] {
				res.adjList[rootWord].Add(outgoingWord)
			}
		}
	}

	return res
}

func (g Graph) ChildrenOf(node string) util.WordSet {
	return g.adjList[node]
}

func validatePath(letters util.LetterSet, path []string) bool {
	pathSet := util.NewLetterSet(path)

	return len(pathSet) == len(letters)
}

func (g Graph) recFindPaths(letters util.LetterSet, node string, path []string, depth int) []string {
	if validatePath(letters, path) {
		return path
	}
	if depth == maxDepth {
		return nil
	}

	path = append(path, node)

	for outgoing := range g.ChildrenOf(node) {
		res := g.recFindPaths(letters, outgoing, path, depth+1)
		if res != nil {
			return res
		}
	}
	path = (path)[:len(path)-1]

	return nil
}

func (g Graph) FindPaths(letters util.LetterSet, numPaths int) [][]string {
	res := make([][]string, 0)

	var maxPaths int
	if numPaths == 0 {
		maxPaths = defaultMaxPaths
	} else {
		maxPaths = numPaths
	}

	for node := range g.adjList {
		path := make([]string, 0)
		temp := g.recFindPaths(letters, node, path, 0)
		if temp != nil {
			res = append(res, temp)
			if len(res) == maxPaths {
				return res
			}
		}
	}

	return res
}
