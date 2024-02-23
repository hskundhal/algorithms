def reverse(array):
    frontindex = 0
    endindex = len(array) - 1
    while frontindex < endindex:
        
        array[frontindex],array[endindex]=array[endindex],array[frontindex]
        
        frontindex+=1
        endindex-=1
    return array

print(reverse([1,2,3,4,5]))
print(reverse([]))