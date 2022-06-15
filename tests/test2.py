def bellman_ford(i):
    node = [float('inf') for x in range(n)]
    node[i] = 0

    Continue = True

    while Continue:
        Continue = False

        for l in range(n):
            for factor in e[l]:
                start = l
                goal  = factor[1]
                cost  = factor[0]

                #更新条件
                if node[start] + cost < node[goal]:
                    node[goal] = node[start] + cost
                    Continue = True
    
    node[i] = float('Inf')
    return node

n,C = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((c, b))
    e[b].append((c, a))

ans = float('inf')
for i in range(n):
    dist = bellman_ford(i)
    for l,j in e[i]:
        dist[j] = float('Inf')
    ans = min(ans, min(dist))
print(ans + C)