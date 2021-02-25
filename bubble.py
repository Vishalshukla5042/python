lis=list(map(int,input("enter list: ").split()))
for i in range(len(lis)):
    for j in range(len(lis)-1-i):
        if lis[j]>lis[j+1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
        
print("sorted list: ",end="")
for ele in lis:
    print(ele,end=" ")
    