import heapq

def LIFO_FF(k, n, m, requests,T):
        
    CachLIFO=[] 
    
    CachFF=set()
    #CachFF=[]
    
    heap=[]
    LIFO=0
    FF=0
    for i in requests:
        if i in CachLIFO:
            LIFO+=1
        else:
            if len(CachLIFO)<k:
                CachLIFO.append(i)
            else:
                CachLIFO[-1]=i
    
    
    P=[1]*(n+1)
    
    
    for i in range(m):
        current_page=requests[i]
        P[current_page]+=1
        
        
        if current_page in CachFF:
            FF+=1
            next_time=T[current_page][P[current_page]-1]
            heapq.heappush(heap, (-next_time,current_page)  )

        else:
            if len(CachFF)<k:
                next_time=T[current_page][P[current_page]-1]
                heapq.heappush(heap, (-next_time,current_page)  )
                CachFF.add(current_page)
                
            else:
                time,page_evict=heapq.heappop(heap)
                CachFF.remove(page_evict)
                
                
                next_time=T[current_page][P[current_page]-1]
                heapq.heappush(heap, (-next_time,current_page)  )
                CachFF.add(current_page)
                
                
        
    summ=(m-FF)+(m-LIFO)   
    dif= (m-LIFO)-(m-FF)         
                
                
    return summ, dif


def read_input():
    k, n, m = map(int, input().split())
    requests = []
    
    for _ in range(m):
        request = int(input())
        requests.append(request)
        
        
    T={i+1:[] for i in range(n)}           
    for i in range(len(requests)):
        T[requests[i]].append(i+1)
        
    for i in T:
        T[i].append(float('inf'))     
        
    return k, n, m, requests,T


if __name__ == "__main__":
    k, n, m, requests,T = read_input()
    summ, dif = LIFO_FF(k, n, m, requests,T)
    print(summ)
    print(dif)
