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

