def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def merge_sort(a):
    n1 = len(a) // 2
    a1 = a[:n1]
    a2 = a[n1:]

    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)

    return merge_list(a1, a2)
