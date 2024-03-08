# Integration of MergeSort and Insertion Sort(HybridSort) #

## Introduction ##
In Mergesort, when the sizes of subarrays are small, the overhead of many recursive
calls makes the algorithm inefficient. Insertion sort, on the other hand is efficient for a small sized-input.

Our goal is to combine Mergesort with Insertion Sort to come out with a more efficient hybrid sorting algorithm.

The idea is to set a small integer S as a threshold for the size of subarrays. S will be used to determine the point at which the algorithm switches from Mergesort to Insertion sort.

When the size of a subarray in a recursive call of Mergesort is less than or equal to S, the algorithm will switch to Insertion Sort.

## Contents ##
 
1. Algorithm implementation
2. Algorithm analysis ( Theoretical and Empirical )
3. Comparison between the Hybrid algorithm and the Mergesort algorithm

## 1. Algorithm Implementation ##

Here is the pseudocode for the Hybrid algorithm:
```
hybridSort(arr, S) 
{
    if (size of arr <= 1)
    {
        return;
    }
    //Here we add in another condition to check the size of the array, when the size if smaller or equal than S, we switch to insertion sort.
    else if (size of arr <= threshold S)
    {
        insertionSort(arr);
    }
    else 
    {
        Partition list into two (approx.) equal sized arr, Left & Right;
        hybridSort (Left);
        hybridSort (Right);
        merge the sorted Left & Right;
	  }
}
The merge function in hybridSort will be the same as the merge function in the original MergeSort.
```
The implementation of HybridSort in Python can be found in [hybridsort.py](https://github.com/jjiunnbeh/SC2001/blob/main/Project%201/src/hybridsort.py), the implementation of the original MergeSort in Python can be found in [mergesort.py](https://github.com/jjiunnbeh/SC2001/blob/main/Project%201/src/mergesort.py). The HybridSort is essentially a MergeSort with an additional conditon. A threshold value, S needs to be set and when the input size is less than or equal to S, Insertion Sort will be used instead of MergeSort.

## 2. Algotithm Analysis ##

### Theoretical Analysis ###
For the original **MergeSort**, the theoretical time complexity is:

The Best Case: O(Nlog(N))  
The Worst Case: O(Nlog(N))  

For the **InsertionSort**, the theoretical time complexity is:  
  
Best Case: O(N)
Worst Case: O(N^2)

Integrating them together, we form the **HybridSort**:

Best Case: O((N/S) x (S) + Nlog(N/S)) = O(N + Nlog(N/S))  
Worst Case: O((N/S) x S^2 + Nlog(N/S)) = O(NS + Nlog(N/S))  
where (N/S) is the number of subarrays with size S, S is the size of the subarrays that will undergo InsertionSort.


To make analysis of the algotithm, we generate arrays of increasing sizes, in a range from 1000 to 1 million. A random dataset of integers is generated in the range from 1 to x, where x is the largest integers that is allowed in the datasets.

```
import random
def generate_random_dataset(size):
    return [random.randint(1,x) for _ in range(size)]
  
input_sizes = list(range(1000,1000000,1000)
for size in sizes:
    dataset = generate_random_dataset(size)
    
```

Our analysis of the algotithms can be found in [Analysis of HybridSort](https://github.com/jjiunnbeh/SC2001/blob/main/Project%201/src/Analysis%20of%20the%20integration%20of%20MergeSort%20and%20InsertionSort%20(HybridSort).ipynb).

Based on the results we obtained, our optimal value of **S = 7**. This is the value we used to compare the performance of the HybridSort algorithm and the original MergeSort algorithm. 10 trials were taken for the input size **N=10000000** and the average key comparisons and time taken were recorded down for comparisons to be made. According to the result, the number of key comparisons and time taken for HybridSort are both lower than that of MergeSort.  
  
With that, we conclude that HybridSort with an optimal value S = 7 will perform better than the original MergeSort.

