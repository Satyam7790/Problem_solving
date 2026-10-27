
# so one method which i see here is that ,
# with backtracking we can make all the subarrays and store their squares in a variable and sum it up . 
# though that feels very greedy .


# arr = [1,2,3,4,5]

# def backtrack(arr):
#     ans = []
#     def haha(i):
#         nonlocal ans 
#         if i >= len(arr):
#             print(ans)
#             return 
#         ans.append(arr[i])
#         haha(i+1)
#         ans.pop()
#         haha(i+1)
#     haha(0)
#     return ans 
# backtrack(arr)







arr = [1,2,3,4,5]

# def backtrack(arr,i):
#     if i >= len(arr):
#         print(arr)
#         return 
    
#     backtrack(arr,i+1)
# backtrack(arr,0)

def backtrack(arr):
    ans = []
    def haha(i):
        nonlocal ans 
        if i >= len(arr):
            print(ans)
            return 
        ans.append(arr[i])
        haha(i+1)
        ans.pop()
        haha(i+1)
    haha(0)
    return ans

backtrack(arr)
    



















