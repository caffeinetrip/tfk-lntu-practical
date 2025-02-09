l = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']


def rd(l1):
    c = {}
    for i in l1:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    
    l1 = [i for i, count in c.items() if count == 1]
    
    return l1

def sl(l1):

    nums = sorted([i for i in l1 if isinstance(i, int)])
    strs = sorted([i for i in l1 if isinstance(i, str)], key=str.casefold)
    

    return nums + strs


l2 = rd(l)


print(l2)
print(sl(l2))