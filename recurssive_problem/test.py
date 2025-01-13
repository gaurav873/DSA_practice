from typing import List

def team(skill: List[int], n: int) -> int:
    inversion_count = 0
    
    def merge_sort(a: List[int]) -> None:
        nonlocal inversion_count
        if len(a) > 1:
            mid = len(a) // 2
            sublist1 = a[:mid]
            sublist2 = a[mid:]
            
            merge_sort(sublist1)
            merge_sort(sublist2)

            i = j = k = 0
            while i < len(sublist1) and j < len(sublist2):
                if sublist1[i] <= sublist2[j]:
                    a[k] = sublist1[i]
                    i += 1
                else:
                    # Count inversions for the current element in sublist2
                    if sublist1[i] >= 2 * sublist2[j]:
                        inversion_count += (len(sublist1) - i)
                    a[k] = sublist2[j]
                    j += 1
                k += 1
            
            while i < len(sublist1):
                a[k] = sublist1[i]
                k += 1
                i += 1
            
            while j < len(sublist2):
                a[k] = sublist2[j]
                k += 1
                j += 1

    merge_sort(skill)
    return inversion_count

# Example usage
skill_levels = [4, 1, 2, 3, 1]
n = len(skill_levels)
result = team(skill_levels, n)
print("Number of valid inversions:", result)


 