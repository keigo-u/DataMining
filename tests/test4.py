inputList = input().split()
asdist = {}
m = int(inputList[-1])
for i in range(len(inputList) - 1):
    a,s = inputList[i].split(":")
    asdist[int(a)] = s

ans = {}
for i in asdist.keys():
    if m % i == 0:
        ans[i] = asdist[i]

sorted_ans = sorted(ans.items(), key=lambda x:x[1])

if len(sorted_ans) == 0:
    print(m)
else:
    for i in sorted_ans:
        b = i[1]
        print(b, end="")
print()
