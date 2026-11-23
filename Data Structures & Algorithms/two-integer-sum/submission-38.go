func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	result := []int{}
	for i := range nums {
		searching := target - nums[i]
		value, ok := hash[searching]

		if !ok {
			hash[nums[i]] = i
		} else {
			result = []int{value, i}
			break
		}
	}
	return result
}
