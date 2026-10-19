nums = list(map(int,input().split()))

def sums(num):
    x = 0
    while num > 0 :
        x += num %10
        num //= 10 
    return x 

def check(num):
    num = str(num)
    return num[0]


swap = 0 

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if sums(nums[i]) > sums(nums[j]) :
            nums[i] , nums[j] = nums[j] , nums[i]
            swap += 1
        if sums(nums[i]) == sums(nums[j]) :
            if check(nums[i]) > check(nums[j]):
                nums[i] , nums[j] = nums[j] , nums[i] 
                swap += 1
print(swap)






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
