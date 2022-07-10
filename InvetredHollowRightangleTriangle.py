# Q1 f.

# 1 2 3 4 5 
# 2     5
# 3   5
# 4 5
# 5

for i in range(1,6):
    for j in range(i,6):
        if(i==1 or j==5 or j==i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

# OR

for i in range(1,6):
    for j in range(1,7-i):
        if(i==1 or j==1 or j==6-i):
            print(i+j-1,end=" ")
        else:
            print(" ",end=" ")
    print()    
