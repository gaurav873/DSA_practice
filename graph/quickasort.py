a=[4,6,2,4,5,9,1]

def partition(data_list,left,right):
    pivot=data_list[left]
    i=left+1
    j=right
    while i<=j:
        while i<=j and data_list[i]<=pivot:
            i+=1
        while i<=j and data_list[j]>pivot:
            j-=1
        if i<j:
            data_list[i],data_list[j]=data_list[j],data_list[i]  
            i+=1
            j-=1
    if i>j:
        data_list[left],data_list[j]=data_list[j],data_list[left]
        print(j)
    return j

# that funtion is use for recurssion 
def quicksort(data_list,left,right):
    if left<right:
        pivot=partition(data_list,left,right)
        quicksort(data_list,left,pivot-1)
        quicksort(data_list,pivot+1,right)
def _quicksort(data_list):
    quicksort(data_list,0,len(data_list)-1)
    return data_list
print(_quicksort(a))

#def quicksort(left,right):
    #left=





        
        
    

        
            
            


            
            
            
        
            
            
        
            







    