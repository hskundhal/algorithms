# space complexity O(n) 
#  time complexity O(n log n) where O(n) for while loops to merge data
# and O(log n) for division into mulitple small sets so 8 items get breaken in three steps to single items

def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([3,1,4,2]))

