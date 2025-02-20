def solve(sequence1, sequence2):
    # ----------------------------- #
    n=len(sequence1)
    m=len(sequence2)
    opt={}
    pi={}
    for j in range(m+1):
        opt[(0,j)]=0
    
    for i in range(1,n+1):
        opt[(i,0)]=0
        for j in range(1,m+1):
            if sequence1[i-1]==sequence2[j-1]:
                opt[(i,j)]=opt[(i-1,j-1)]+1
                pi[(i,j)]="d"
            elif opt[(i,j-1)]>=opt[(i-1,j)]:
                opt[(i,j)]=opt[(i,j-1)]
                pi[(i,j)]="l"
            else:
                opt[(i,j)]=opt[(i-1,j)]
                pi[(i,j)]="u"
    
            
    LCS=opt[(n,m)]
    
    S=[]
    i=n-1
    j=m-1
    while i>=0 and j>=0:
        if pi[(i+1,j+1)]=="d":
            S.append(sequence1[i])
            i-=1
            j-=1
                
        elif pi[(i+1,j+1)]=="u":
            i-=1
        else:
            j-=1
            
    S.reverse()
    
    I=0
    J=0
    for i in range(n):
        if sequence1[i]!= S[0]:
            I+=1
        else:
            break
    
    for j in range(m):
        if sequence2[j]!= S[0]:
            J+=1
        else:
            break
        
    length=len(sequence1[I:])+ len(sequence2[J:])
    sequence12=sequence1[I:]
    sequence22=sequence2[J:]
    
    return LCS,length
         

def read_input():
    sequence1 = input().lower()
    sequence2 = input().lower()
    return sequence1, sequence2



sequence1,sequence2=read_input()
LCS,length=solve(sequence1, sequence2)
print(LCS)
print(length)

