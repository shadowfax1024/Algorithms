def count_sort(A,exp1):
    len_A = len(A)
    result = []*len_A
    count = []*10
    for _ in range(max_A):
        result.append([])
    for a in A:
        print(a,result[a])
        result[a].append(a)
    print(result)
    final= []
    for i in range(max_A+1):
        if(result[i] != []):
            final.extend(result[i])
    return final

def radix_sort(A):
    max_A = max(A)
    print("max in the array :", A)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
 