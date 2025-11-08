def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def sift_down(arr, i, upper):
    while True:
        lef, rig = i * 2 + 1, i * 2 + 2

        if rig < upper:
            if arr[i] >= max(arr[lef], arr[rig]):
                return
            if arr[lef] > arr[rig]:
                swap(arr, i, lef)
                i = lef
            else:
                swap(arr, i, rig)
                i = rig

        elif lef < upper:
            if arr[lef] > arr[i]:
                swap(arr, i, lef)
                i = lef
            else:
                return

        else:
            return


def heap_sort(arr):
    for j in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, j, len(arr))

    for end in range(len(arr) - 1, 0, -1):
        swap(arr, 0, end)
        sift_down(arr, 0, end)
    return arr
