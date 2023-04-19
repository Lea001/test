def search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = left + ((right - left) // 2)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else :
            return(mid)
    return(-1)

nums = [-1,0,2,5,8,9]
target = 10
print(search(nums,target))
