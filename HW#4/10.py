def crte_2d_arr(rows, columns):
    # create a 2d array
    arr = []
    for i in range(rows):
        arr.append([])
        for j in range(columns):
            arr[i].append('-')
    return arr

print("crte_2d_arr(3,5):", crte_2d_arr(3,5))
print("crte_2d_arr(2,4):", crte_2d_arr(2,4))
print("crte_2d_arr(5,2):", crte_2d_arr(5,2))
