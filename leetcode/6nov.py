# n = 3
# logs = [[2,4],[2,1],[1,2],[3,1]]
# x = 2
# queries = [3,4]
# checker = 0
# final_ans = []
# full_cnt = n
# actual_cnt = 0
# actual_cnt_array = []

# for i in range(len(queries)):
#     ans = 0
#     checker = queries[i] - x 
#     truth = [False] * len(logs)
#     m = 0

#     for j in range(len(logs)):
#         if logs[j][0] not in actual_cnt_array :
#             actual_cnt_array.append(logs[j][0])
#             actual_cnt += 1      
#         if (logs[j][1] < checker or logs[j][1] > queries[i]) and truth[logs[j][0]] == True :
#             continue
#         if (logs[j][1] >= checker or logs[j][1] <= queries[i]) and truth[logs[j][0]] == True :
#             ans -= 1
#         if (logs[j][1] < checker or logs[j][1] > queries[i]) and truth[logs[j][0]] == False :
#             truth[logs[j][0]] = True
#             ans += 1
#         if (logs[j][1] >= checker or logs[j][1] <= queries[i]) and truth[logs[j][0]] == False :
#             truth[logs[j][0]] = True 

#     m = (n-actual_cnt) + ans 
#     final_ans.append(m)

# print(final_ans)
# rather than checking for valid soln checking for invalid ids then subtracting from full will also giev the correct ids 



n = 3
logs = [[2,4],[2,1],[1,2],[3,1]]
x = 2
queries = [3,4]
checker = 0
final_ans = []
full_cnt = n
actual_cnt = 0
actual_cnt_array = []

for i in range(len(queries)):
    ans = 0
    checker = queries[i] - x 
    truth = [False] * len(logs)
    m = 0

    for j in range(len(logs)):
        if logs[j][0] not in actual_cnt_array:
            actual_cnt_array.append(logs[j][0])
            actual_cnt += 1

        if (logs[j][1] < checker or logs[j][1] > queries[i]):
             continue

        if (logs[j][1] >= checker and logs[j][1] <= queries[i]) and truth[logs[j][0]] == False:
            truth[logs[j][0]] = True
            ans += 1

    m = n - ans
    final_ans.append(m)

print(final_ans)



