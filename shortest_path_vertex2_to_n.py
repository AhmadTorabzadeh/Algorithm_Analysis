def shortest_path(n,edges):
    F={i:float('inf') for i in range(1,n+1)}
    F[2]=0
    for l in range(1,n+1):
        updated=False
        for e in edges:
            if F[e[0]]+e[2]<F[e[1]]:
                F[e[1]]=F[e[0]]+e[2]
                updated=True
        if not updated:
            SP=F[n]
            return SP

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, edges



n,m,edges=read_input()

SP=shortest_path(n, edges)
if SP==float('inf'):
    SP="INFINITY"
print(SP)




# 5 5
# 1 2 2
# 1 3 -1
# 2 3 2
# 2 4 3
# 3 5 4