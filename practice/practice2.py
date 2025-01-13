def majorityElement(v: list[int]) -> [int]:
    can1,can2=None,None
    cnt1,cnt2=0,0
    n=len(v)
    ls=[]# result
    for element in range(n):
        if cnt1==0 and v[element]!=can2:
            can1=v[element]
            cnt1+=1
        elif cnt2==0 and v[element]!=cnt1:
            can2=v[element]
            cnt2+=1
        elif v[element]==can1:
            cnt1+=1
        elif v[element]==can2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    cnt1,cnt2=0,0
    for x in range(n):
        if v[x]==can1:
            cnt1+=1
        if v[x]==can2:
            cnt2+=1
    check=n//3
    if cnt1>check:
        ls.append(can1)
    if cnt2>check:
        ls.append(can2)
    return sorted(ls)
arr = [11, 33, 33, 11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()


             
         

 

  