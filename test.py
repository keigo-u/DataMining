import matplotlib.pyplot as plt
import networkx as nx

N,C = map(int, input().split())
G = nx.Graph()
G.add_nodes_from([i+1 for i in range(N)])

edge = []
am = [[0]*N for _ in range(N)]
for _ in range(N-1):
    u,v,w = map(int, input().split())
    x = [u,v,w]
    edge.append(x)
    am[u-1][v-1] = w
    am[v-1][u-1] = w
G.add_weighted_edges_from(edge)

data = []
for i in range(N):
    for j in range(i+1,N):
        if am[i][j] == 0:
            x = [i, j, nx.dijkstra_path_length(G, i+1, j+1)]
            data.append(x)

score = []
for i in range(len(data)):
    score.append(data[i][2])
min_score_index = score.index(min(score))

print(data[min_score_index][2] + C)