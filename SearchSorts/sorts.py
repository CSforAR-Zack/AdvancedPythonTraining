#sorts.py

from time import time

#Selectrion Sort

def selSort(nums):
    #sort nums into ascending order

    n = len(nums)

    #For each position in the list (except the very last)
    for bottom in range(n-1):

        mp = bottom 
        for i in range(bottom + 1, n):
            if nums[i] < nums[mp]:
                mp = i
                
        temp = nums[mp]
        nums[mp] = nums[bottom]
        nums[bottom] = temp


#Merg Sort (Divide and Conquer)
def merge(lst1, lst2, lst3):
    #merge sorted lsits lst1 and lst2 into lst3
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)

    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1

    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1

    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(nums):
    n = len(nums)

    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2, nums)
    
s = [4,7,8,3,5,4,1,2,9,0,5,67,58,43,90,100,31,7,85]
t = [4,7,8,3,5,4,1,2,9,0,5,67,58,43,90,100,31,7,85]
r = [4,7,8,3,5,4,1,2,9,0,5,67,58,43,90,100,31,7,85]

tS1 = time()
selSort(s)
print(time() - tS1)
print(s)

tM1 = time()
mergeSort(t)
print(time() - tM1)
print(t)

tR1 = time()
r.sort()
print(time() - tR1)
print(r)
