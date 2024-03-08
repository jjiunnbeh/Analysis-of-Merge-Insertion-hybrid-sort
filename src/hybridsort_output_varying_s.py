import csv
import random
import time

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
    keycmp=0
    if len(arr) <= 1:
        if len(arr) ==1:
            return 1
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


# Merge function 
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
def generate_random_dataset(size):
    return [random.randint(1, x) for _ in range(size)]
#size fixed at 10 million
size = 10000000
trials = 10
x = 100000

with open('hybridsort_output_varying_S.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["S", "Average Key Comparisons", "Average Time Taken"])

    # Different values of S from 1 to 100
    for S in range(1, 101):
        keycmp_total = 0
        time_taken_total = 0

        for _ in range(trials):
            dataset = generate_random_dataset(size)
            start = time.time()
            keycmp = hybridsort(dataset, S)
            end = time.time()
            time_taken = end - start

            keycmp_total += keycmp
            time_taken_total += time_taken

        # Get average key comparisons and time taken
        average_keycmp = keycmp_total / trials
        average_time_taken = time_taken_total / trials

        writer.writerow([S, average_keycmp, average_time_taken])

# Successful CSV creation message
print("Results saved in hybridsort_output_vary_S.csv")