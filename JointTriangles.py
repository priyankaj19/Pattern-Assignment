# Q1 h.

# 1               1 
# 1 2           2 1
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3 4 5 4 3 2 1

k=7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,k+1):
        print(" ",end=" ")
    k-= 2
    for j in range(i,0,-1):
        if (i==5 and j==5):
            print("",end="")
        else:
            print(j,end=" ")
    print()

# OR
m=0
for i in range(1,6):
    k=i+m 
    for j in range(1,i+1):
        if(i==5 and j==5):
            print("",end="")
        else:
            print(j,end=" ")
    for j in range (8,k,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
        i-=1
    m+=1
    print()
