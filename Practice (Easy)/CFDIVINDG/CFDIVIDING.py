def dividingStamps(array, numberOfMembers):
    stampSum = idxSum = 0
    
    for idx, stamps in enumerate(array,1):
        stampSum += stamps
        idxSum += idx
        #print(str(idx)+ ":::"  +str(stamps))
    #print(stampSum)
    if stampSum == idxSum:
        return True
    else:
        return False

        
    

numberOfMembers = map(int, input().strip().split(' '))
array = list(map(int, input().strip().split(' ')))
answer = dividingStamps(array, numberOfMembers);
if answer:
    print("YES")
else:
    print("NO")
