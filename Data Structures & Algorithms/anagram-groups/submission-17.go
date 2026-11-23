import (
	"slices"
)

func groupAnagrams(strs []string) [][]string {
	//O (n*m) time and O(m) space where m is numbers and n the length
	//Iterar sobre todos os elemnetos
	//Para cada elemento, eu o ordeno
	//Subo o hash key no meu map ordenado dentro de uma lista, e nessa lista, appendo o meu index originario
	//Itero final sobre o map montando o resultado.
	hash := make(map[string][]string)
	for _, str := range strs {
		runes := []rune(str)
		slices.Sort(runes)
		sorted := string(runes)
		value, ok := hash[sorted]
		if !ok {
			hash[sorted] = []string{str}
			continue
		} else {
			hash[sorted] = append(value, str)
		}
	}

	final_result := [][]string{}
	for _, value := range hash {
		final_result = append(final_result, value)
	}
	return final_result
}
