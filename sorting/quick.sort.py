# quick Sort---> ismain (n-1)number of steps honge jo ek ek buble compare hoga
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-1):
            if data_list[i]> data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
    return data_list
def modified_bubbleSort(data_list):
    swapped=False
    for r in range(1,len(data_list)):
        swapped=False
        for i in range(len(data_list)-1):
            if data_list[i]> data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                swapped=True
        if swapped==False:
            break
# driven code
l=[21,12,34,98,45,53]
modified_bubbleSort(l)
print(l)
# selection sort--->
def Selection_sort(data_list):
    #  step1--->first find smallest number in list/array
    for r in range(len(data_list)):
        pos=r   # hum ismain position store karenge jisko exchange karenge
        small=data_list[r] 
        for num in range(r+1,len(data_list)):
            if data_list[num]<small:
                small=data_list[num]
                pos=num
        data_list[r],data_list[pos]=data_list[pos],data_list[r]       
    return data_list
def Quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    pivot=data_list[0]
    low=[x for x in data_list[1:] if x<=pivot]
    high=[x for x in data_list[1:] if x>pivot]
    return Quick_sort(low)+[pivot]+Quick_sort(high)
    # driven code
data = [5, 4, 1, 2, 3]
print(Quick_sort(data))       
    

















        