def trappedwater(array):
    i=0
    k=len(array)-1
    left_max=[0]
    right_max = [0]
    water = []
    ll = 0
    rr = 0
    for m in range(len(array)-1):
        # print (m)
        if array[m]> ll:
            ll= array[m]
        left_max.append(ll)
        if array[len(array)-m-1]> rr:
            rr=array[len(array)-m-1]
        right_max.append(rr)
    right_max.reverse()
    # print(right_max)
    # print(left_max)
    
    for k in range(len(array)):
        border = min(left_max[k],right_max[k])
        # print(border)
        if (border-array[k]) > 0:
            water.append(border-array[k])
        else:
            water.append(0)
        
    return water


if __name__ == '__main__':
    print(trappedwater([1,2,1,4,2,3]))