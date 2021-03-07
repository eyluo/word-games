package util

const (
	numSides       = 4
	lettersPerSide = 3
	numLetters     = numSides * lettersPerSide
)

type LetterSet map[rune]int

func NewLetterSet(letters []string) LetterSet {
	res := make(map[rune]int)
	for i, word := range letters {
		for _, letter := range word {
			res[letter] = i
		}
	}

	return res
}

func (l LetterSet) IsLegalSquare() bool {
	return len(l) == numLetters
}

func (l LetterSet) CanMakeWord(word string) bool {
	prevLetterIndex := -1
	for _, letter := range word {
		letterIndex, ok := l[letter]
		if !ok {
			return false
		} else if letterIndex == prevLetterIndex {
			return false
		}

		prevLetterIndex = letterIndex
	}

	return true
}
