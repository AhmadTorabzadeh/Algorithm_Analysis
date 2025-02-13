def interval_scheduling_coving(n, u, v, intervals):
    # Please write your algorithm here:
    S=[]
    t=0
    t_prime=u
    Min=[]

    for i in range(n):
        if intervals[i][0]>=t:
            S.append(i)
            t=intervals[i][1]
    maximum=len(S)
    
    

    while len(intervals)!=0 and t_prime<=v:
        P=[]
        for i in range(len(intervals)):
            
            if intervals[i][0]<=t_prime:
                P.append(intervals[i])
            
       # j= max(enumerate(P), key=lambda x: x[1][1])[0]  
        
        if len(P)!=0:
            t_prime=P[-1][1]    
            Min.append(P[-1])
            for k in P:
                intervals.remove(k)
        else:    
            return maximum, "no" 
        
    minimum=len(Min)
    
    return maximum, minimum


def read_input():
    n,u,v=map(int,input().split())
    while n>10000:
       n,u,v=map(int, input().split())
    
    intervals=[]
    for i in range(n):
        s,f=map(int,input().split())
        intervals.append((s,f))
    intervals=sorted(intervals, key=lambda x: x[1])    
    return n,u,v,intervals



n,u,v,intervals=read_input()

#print(intervals)
maximum,minimum=interval_scheduling_coving(n, u, v, intervals)

print(maximum)
print(minimum)

