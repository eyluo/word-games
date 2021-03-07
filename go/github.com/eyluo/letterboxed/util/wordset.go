package util

type WordSet map[string]bool

func NewWordSet(words []string) WordSet {
	res := make(map[string]bool)
	for _, word := range words {
		res[word] = true
	}

	return res
}

func (w WordSet) Has(word string) bool {
	return w[word]
}

func (w WordSet) Add(word string) {
	w[word] = true
}
