# nums = list(map(int,input().split()))
# a = nums.copy()
# def sums(num):
#     x = 0
#     while num > 0 :
#         x += num %10
#         num //= 10 
#     return x 

# def check(num):
#     num = str(num)
#     return num[0]


# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if sums(nums[i]) > sums(nums[j]) :
#             nums[i] , nums[j] = nums[j] , nums[i]

#         if sums(nums[i]) == sums(nums[j]) :
#             if check(nums[i]) > check(nums[j]):
#                 nums[i] , nums[j] = nums[j] , nums[i]

# ans = 0
# for k in range(len(nums)):
#     if a[k] != nums[k]:
#         ans += 1 
# print(ans//2)

# print(a)
# print(nums)
arr1 = [18,43,34,16]
arr2 = [16,34,43,18]
n = len(arr1)

for i in range(n):
    ans = []
    visited = [False]*(n)
    for j in range(n):
        if arr1[i] == arr2[j]:
            visited[i] == True
            visited[j] == True 
            ans.append(i)
            ans.append(j)
    print(ans)

ans=[]
lis=[]
def recur(i,arr):
    if i==len(arr):
        ans.append(lis)
        return 
    lis.append(arr[i])
    recur(i+1,lis,arr)
    lis.pop()
    recur(i+1,lis,arr)

        























# arr.sort()
# l = []
# for i in range(len(nums)):
#     l.append(sums(nums[i]))
# print(l)

# b = l.sort()
# if l == b :
#     swap = 0

# for j in range(len(nums)):




# logic is brute force n max swao isnt wrong ;)
# k-1 swap concept 