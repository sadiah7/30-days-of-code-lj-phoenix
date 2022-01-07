arr1 = [1, 2, 3, 4, 5]
arr2 = [7, 8, 9, 1, 2, 3, 4, 12, 13]


def compute(arrb, arrs):
    ans = arrb
    for i in arrs:
        if i not in arrb:
            ans.append(i)
    return ans


if len(arr1) < len(arr2):
    print(len(compute(arr2, arr1)))

else:
    print(len(compute(arr1, arr2)))
