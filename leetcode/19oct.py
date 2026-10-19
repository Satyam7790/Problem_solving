nums = sorted(list(map(int,input().split())))
target = int(input())

ans = []

for i in range(len(nums)):
    if nums[i] == target :
        ans.append(i)
print(ans)


# arr = [1,2,3,4,5]
# a = map(str,arr)

# b = list(a)
# print(b)