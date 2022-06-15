import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [float('inf')] * n
    cost[s] = 0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    cost[s] = float('inf')
    return cost

n,C = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((c, b))
    e[b].append((c, a))

ans = float('inf')
for i in range(n):
    dist = dijkstra(i)
    print(dist)
    for l,j in e[i]:
        dist[j] = float('Inf')
    ans = min(ans, min(dist))
print(ans + C)

print(e)
opt_node = bellman_ford(1)
print(opt_node)
exit()