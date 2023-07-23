def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[start]:
                continue
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result


nums = [1, 1, 2]
print(permute_unique(nums))
