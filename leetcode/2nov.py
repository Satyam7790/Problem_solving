nums = list(map(int,input().split())) 
a = nums.copy()
a.sort()
maxy = a[-1]

def add(nums):
    cost_add = 0 
    for i in range(len(nums)):
        cost_add += maxy - nums[i]
    return cost_add

def mid(nums):
    cost_mid = 0
    x = len(nums)
    mid = a[x//2]   
    for j in range(len(nums)):
        cost_mid += abs(mid - nums[j])
    return cost_mid
    
def ans(nums):
    return min(add(nums),mid(nums))
print(ans(nums))

    