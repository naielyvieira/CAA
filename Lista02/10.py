def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Exemplo de uso:
nums1 = [1, 3, 5, 6]
target1 = 5
print(search_insert(nums1, target1))

nums2 = [1, 3, 5, 6]
target2 = 2
print(search_insert(nums2, target2))
