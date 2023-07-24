def robber(array):
    temp=0
    temp2=0
    i=0
    j=1
    while(i<len(array)):
        temp+=array[i]
        i+=2
    while(j<len(array)):
        temp2+=array[j]
        j+=2
    return max(temp,temp2)
array=list(map(int,input().split()))
print(robber(array))