import sys
sys.stdin = open('ip.txt','r')
sys.stdout = open('op.txt','w')


adj = [[1,0],[2,0],[0,5],[5,4],[4,3],[4,6]]

graph = {}
edges = len(adj)

for k,v in adj:

    if graph.get(k):
        graph[k].append(v)
    else :
        graph[k] = [v]

    if graph.get(v):
        graph[v].append(k)
    else :
        graph[v] = [k]

for k,v in graph.items() :
    print(k,v)
    

class GraphAPI:
    pass