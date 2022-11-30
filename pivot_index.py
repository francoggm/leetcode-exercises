def pivotIndex(nums):
    for i, n in enumerate(nums):
        left = sum(nums[:i]) if i != 0 else 0
        right = sum(nums[i+1:]) if i != len(nums) - 1 else 0 
        if left == right:
            return i
    return -1

pivotIndex([1,7,3,6,5,6])