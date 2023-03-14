def arr_soma(arr):
    if arr == []:
        return 0
    return arr[0] + arr_soma(arr[1:])

tes = [9, 3, 5, 1, 2]

def rec_count(arr):
    if arr == []:
        return 0
    return 1 + rec_count(arr[1:])
    

def maior_number(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        return arr[1]
    sub_lis = maior_number(arr[1:])
    print(arr[0])
    if arr[0] > sub_lis:
        return arr[0]
    return sub_lis

    

print(maior_number(tes))
    
    
