func hasDuplicate(nums []int) bool {
	hash := make(map[int]struct{}, len(nums))
	for _, v := range nums {
		_, ok := hash[v]
		if ok {
			return true
		}
		hash[v] = struct{}{}
	}
	return false
}