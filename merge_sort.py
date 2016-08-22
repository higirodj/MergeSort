#!/usr/bin/python

def mergeSort(a):
    
    # n is the length of the array a
    n = len(a)
    
    # base case
    if(n<=1):
        return
    
    # Identify the middle index of the array
    # the index is used to divide the array into two parts
    middleIndex = n/2
    
    # fill the left subarray
    leftSubArray = a[0:middleIndex]
        
    # fill the right subarray
    rightSubArray = a[middleIndex:n]
        
    # recursively divide the left part of the subarray
    # into smaller parts
    mergeSort(leftSubArray)
    
    # recursively divide the right part of the subarray
    # into smaller parts
    mergeSort(rightSubArray)
    
    # merge and sort the subarrays into the sorted
    # solution for the original array
    merge(a, leftSubArray, rightSubArray)

def merge(a, left, right):
    
    leftLength = len(left)
    rightLength = len(right)
    i = j = k = 0
    
    # compare elements of left and right arrays and merge
    # into a single array
    while(i < leftLength and j < rightLength):
        
        # case where element in left array is less or equal to
        # the element in right array
        if(left[i] <= right[j]):
            a[k] = left[i]
            i+=1
        
        # case where element in right array is greater than
        # the element in left array
        else:
            a[k] = right[j]
            j+=1
    
        k=k+1

    # two possible situations may arise during sort: situation 1 or 2 but not both.

    # situation 1: case where there exists elements that are leftover in left array
    # insert into the merged array
    while(i < leftLength):
        a[k] = left[i]
        i+=1
        k+=1

    # situation 2: case where there exists elements that are leftover in right array
    # insert into the merged array
    while(j < rightLength):
        a[k] = right[j]
        j+=1
        k+=1
        
def main():
    
    data = [3,7,5,9,2,8,10,6,-9,4,1]
    mergeSort(data)
    print(data)
    
main()        
