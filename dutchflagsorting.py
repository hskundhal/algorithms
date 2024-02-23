def dutchflagsort(array):
    i = 0
    j = 0
    k = len(array)-1
    mid = 1
    while (j < k):

        if (array[j]<mid):
            array[i],array[j] = array[j],array[i]
            i+=1
            j+=1
        elif array[j]==mid:
            
            j+=1
        elif array[j]>mid:
            array[j],array[k]=array[k],array[j]
            k-=1
            
    print(array)



if __name__ == '__main__':
    dutchflagsort([1,1,2,0,1,0])