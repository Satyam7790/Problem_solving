import math 
# some things ive deduced :
# if u have a number n and u want minimum number of places of a number say x needed such 
# that sum of all digits of x sums to n , then that would be ceil(n/9) ;
# And if asked maximum number of places of a number say x needed such 
# that sum of all digits of x sums to n then that would be infinite ;

# now here a constraint is added to reduce the max num from infinite to some number 

# now we know one thing that max number of digit is fixed say 
# for example num = 2 and sum = 5 
# so there are only two places and sum of those two places should be 5 
# for our number to be max our last digit (first from left(i forgot :)) shoudl be max 
# so at first well place max number possible , it would be 9 for sums > 9 

nums , sums = map(int,input().split())

flag = True 
ans = ""

if sums <= 9 :
    ans += str(sums)
    for i in range(nums-1):
        ans += str(0)
    print(ans)
elif nums < math.ceil(sums/9):
    print("")
else :
    for j in range(nums):
        if sums >= 9 :
            ans += str(9)
            sums -= 9
        else :
            a = sums%9 
            ans += str(a)
            sums -= a 
    print(ans)









