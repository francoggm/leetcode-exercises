nums = [4,5,6,7,0,1,2]
nums = [2, 4, 5, 6, 7, 0, 1]
target = 3

def search(nums, target):
    left, right = 0, len(nums) - 1

    while right >= left:
        mid = (right + left) // 2
        print(mid, left, right)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            #Direita
            left = mid 
        else:
            #Esquerda
            right = mid - 1
    return -1

search(nums, target)