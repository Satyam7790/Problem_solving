nums = [2,1,3]
a = nums.copy()

ans = 0 
a.sort()
b = a[-1]

for i in range(len(nums)):
    ans += b - nums[i]
print(ans)