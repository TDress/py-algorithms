def _isNAD(numpos1, numpos2, k, t):
    pos1, val1 = numpos1
    pos2, val2 = numpos2
    return (abs(pos1 - pos2) <= k) and (abs(val1 - val2) <= t)

def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool

    """
    numpos = [(i, num) for i, num in enumerate(nums)]
    numpos.sort(key=lambda t: t[1])
    for i in range(len(numpos) - 1):
    if _isNAD(numpos[i], numpos[i + 1], k, t):
    return True

    return False

def main():
    l = [1,2,3,1]
    k, t = 3, 0
    assert(containsNearbyAlmostDuplicate(l, k, t))
