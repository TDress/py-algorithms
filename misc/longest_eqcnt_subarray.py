from lib import assertion

def longest_eqcnt_subarray(items):
    if len(items) == 0:
        return []

    nc, cc, cnts = 0, 0, [None] * len(items)
    for i, item in enumerate(items):
        if type(item) == str:
            cc += 1
        else:
            nc += 1
        cnts[i] = (nc, cc)

    for i in range(len(cnts) - 1, -1, -1):
        nc, cc = cnts[i]
        if nc == cc:
            return items[:i + 1]
        diff = abs(nc - cc)
        subnc, subcc = cnts[diff - 1]
        if (cc > nc and subcc == diff) or (cc < nc and subnc == diff):
            return items[diff - 1: i + 1]

    return []

def main():
    l1 = [1,2,3,'a', 'c', 4, 'd', 'e', 'f', 'g', 5]
    l2 = ['a', 1,2,3, 'd']
    assertion.equals([1,2,3,'a', 'c', 4, 'd', 'e'], longest_eqcnt_subarray(l1))
    assertion.equals(['a',1], longest_eqcnt_subarray(l2))

if __name__ == '__main__':
    main()

