def merge_sort(datalist):
    if len(datalist)>1:
        mid=len(datalist)//2
        sublist1=[x for x in datalist[:mid]]
        sublist2=[x for x in datalist[mid:]]
        merge_sort(sublist1)
        merge_sort(sublist2)
        i=j=k=0
        while i<len(sublist1) and j<len(sublist2):
            if sublist1[i]<sublist2[j]:
                datalist[k]=sublist1[i]
                i+=1
            else:
                datalist[k]=sublist2[j] 
                j+=1
            k+=1
        while i<len(sublist1):
            datalist[k]=sublist1[i]
            k+=1
            i+=1  
        while j<len(sublist2):
            datalist[k]=sublist2[j]
            k+=1    
            j+=1
data=[1,4,2,6,9,8,3]
merge_sort(data)
print(data)
        






