def binary_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[2,4,6,8,10,12]
bs=binary_search(arr,8)
print(bs)


        

