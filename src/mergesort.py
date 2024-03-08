def mergesort(arr, S):
    if len(arr) < 1:
        return 0
    else:
        mid = int(len(arr)/2)
        L_arr = arr[slice(None, mid)]
        R_arr = arr[slice(mid, None)]


        L_cmp = mergesort(L_arr,S)
        R_cmp = mergesort(R_arr,S)
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
