#searches.py


#linear search
def linearSearch(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


#binary search looping
def binarySearchLoop(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

#binary search recursive
def binarySearchRecur(item, search_list):
    return binarySearchRecurHelper(item, search_list, 0, len(search_list)-1)

def binarySearchRecurHelper(x, nums, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    item = nums[mid]
    if x == item:
        return mid
    elif x < item:
        return binarySearchRecurHelper(x, nums, low, mid - 1)
    else:
        return binarySearchRecurHelper(x, nums, mid + 1, high)

a = [1,2,3,4,5,6,7,8,9,10,12,12,13,14,15,16,17,25,27,38,49,60,90,100]

print(linearSearch(11,a))
print(binarySearchLoop(11,a))
print(binarySearchRecur(11,a))
