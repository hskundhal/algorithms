

def twosum(nums, target):
    hashmap = {}
    for i,num in enumerate(nums):
        remaining = target - num
        if (remaining in hashmap):
            return [i,hashmap[remaining]]
        hashmap[num]= i
        # print(hashmap)
    return None

print(twosum([17,21,13,4,5,6,6,7,7,8,8,9,0],12)
)
print(twosum([10],12))
print(twosum([],12))