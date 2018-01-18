def dividingStamps(array, numberOfMembers):
    stampSum = idxSum = 0 # int x, y = 0
    for idx, stamps in enumerate(array,1): # Enumerate method saved life
        stampSum += stamps
        idxSum += idx
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
