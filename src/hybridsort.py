def insertionsort(arr) :
    keycmp = 0 
    for i in range (1 , len (arr)) :
        for j in range (i , 0 , -1) :
            keycmp += 1
            if (arr[j] < arr[j - 1]) :
                temp = arr[j] 
                arr[j] = arr[j - 1]
                arr[j - 1] = temp 
            else :
                break
    return keycmp


def hybridsort(arr, S):
    if len(arr) < 1:
        return 0
    else:

        if(len(arr) <= S):
            keycmp = insertionsort(arr)
            return keycmp

        mid = int(len(arr)/2)
        L_arr = arr[slice(None, mid)]
        R_arr = arr[slice(mid, None)]


        L_cmp = hybridsort(L_arr,S)
        R_cmp = hybridsort(R_arr,S)
        keycmp = L_cmp + R_cmp
        i = j = k = 0

        while i < len(L_arr) and j < len(R_arr):
            keycmp+=1
            if L_arr[i] <= R_arr[j]:
                arr[k] = L_arr[i]
                i += 1
            else:
                arr[k] = R_arr[j]
                j += 1
                k += 1
        while i < len(L_arr):
            arr[k] = L_arr[i]
            i += 1
            k += 1

        while j < len(R_arr):
            arr[k] = R_arr[j]
            j += 1
            k += 1
        return keycmp
