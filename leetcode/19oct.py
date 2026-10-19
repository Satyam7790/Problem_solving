nums = sorted(list(map(int,input().split())))
target = int(input())

ans = []

for i in range(len(nums)):
    if nums[i] == target :
        ans.append(i)
print(ans)

