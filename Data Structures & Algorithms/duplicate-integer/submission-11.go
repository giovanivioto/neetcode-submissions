func hasDuplicate(nums []int) bool {
	hash := make(map[int]bool, len(nums))
	for _, v := range nums {
		_, ok := hash[v]
		if !ok {
			hash[v] = true
		} else {
			return true
		}
	}
	return false
}