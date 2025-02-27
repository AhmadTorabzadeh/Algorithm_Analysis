from collections import deque
#input
def read_input():
    
    n, m = map(int, input().split())
    while n>1000 or m>100000:
        n, m = map(int, input().split())
        
    s, t = map(int, input().split())
    while s>n or t>n:
        s, t = map(int, input().split())
        
    edges=[]
    N={i+1:[] for i in range(n)}
    

    for i in range(m):
        u, v = map(int, input().split())
        
        edges.append((u, v))
        N[u].append(v)
        N[v].append(u)
    return n, m, s, t, edges,N



def BFS(N,s,t):
    que=deque([(s,[s])])
    visited=set()
    
    while que:
        (node,path)=que.popleft()
        if node not in visited:
            visited.add(node)
            
            if node==t:
                return "Yes"
            
            for i in N[node]:
                if i not in visited:
                    que.append((i, path+[i]))
                
                    
    return "No"
               

n, m, s, t, edges,N=read_input()

     
        
result1=BFS(N, s, t)

print(result1)


















