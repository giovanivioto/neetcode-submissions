func isAnagram(s string, t string) bool {
    	if len(s) != len(t) {
		return false
	}

	hashS := make(map[rune]int, len(s))
	for _, valueS := range s {
		hashS[valueS] += 1
	}

	hashT := make(map[rune]int, len(t))
	for _, valueT := range t {
		hashT[valueT] += 1
	}

	for k, v := range hashS {
		if v != hashT[k] {
			return false
		}
	}
	return true
}
