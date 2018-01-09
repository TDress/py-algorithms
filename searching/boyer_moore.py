from lib import assertion

def find_boyer_moore(haystack, needle):
    """Use simplified Boyer Moore algorith to find the index of the first 
    occurence of needle in haystack, or -1 if not found
    
    :param haystack: the larger string to be searched.
    :param needle: a string to be found in haystack.

    """
    len_haystack, len_needle = len(haystack), len(needle)
    if len_needle == 0: return 0
    elif len_needle > len_haystack: return -1

    # we depend on a lookup table that has constant time lookups
    # to determine where in needle is the last occurence of a char
    last = {}
    for i in range(len_needle):
        last[needle[i]] = i

    index_h = len_needle - 1
    index_n = len_needle - 1
    while index_h < len_haystack:
        if haystack[index_h] == needle[index_n]:
            if index_n == 0:
                # we have matched every char of needle to one in haystack
                return index_h
            else:
                # keep comparing until we exhaust needle
                index_n -= 1
                index_h -= 1
        else:
            last_needle = last.get(haystack[index_h], -1)
            # advance the haystack character used for comparison.
            # if we didn't find the char in needle anywhere, then advance the 
            # length of needle.  If the last occurence in needle is further in the
            # string than the index of needle we most recently visited for comparison,
            # then only advance so the number of chars we just looked at.
            index_h += len_needle - min(last_needle + 1, index_n)
            index_n = len_needle - 1

    return -1

    
def main():
    s = 'abacaabadcabacabaabb'
    needle = 'abacab'
    assertion.equals(10, find_boyer_moore(s, needle))

if __name__ == '__main__':
    main()

