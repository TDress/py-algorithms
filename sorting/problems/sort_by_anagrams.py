# Sort a list of strings so that strings are gouped by anagrams of each 
# other. ie. we don't care about the ordering except that anagrams are
# adjacent to each other in ouput.

from lib import assertion

def sortByAnagrams(A):
    xor_results = {}
    for s in A:
        res = 0
        for c in s:
            res ^= ord(c)
        try:
            xor_results[res].append(s)
        except KeyError:
            xor_results[res] = [s]

    return [str for strs in xor_results.values() for str in strs]


def main():
    # first test list.  output should have the following anagrams
    # grouped: "ar", "ra"; "abc", "cab" "abcxyz", "xzabcy"
    l1 = [
        "a", "b", "x", "ra", "ab", "ar", "tr", "abc", "gab", "cab", 
        "asdf", "qwer", "qwrx", "asdfgh", "xzabcy", "abcxyz"
    ]
    # grouped: "ab", "ba"; "rt", "tr"; "cab", "bca"; "qwer", "qwre"
    l2 = [
        "a", "b", "qwer", "x", "ab", "ar", "tr", "gab", "cab", 
        "asdf", "qwrx", "asdfgh", "qwre", "ba", "rt", "bca"
    ]

    l1out = sortByAnagrams(l1)
    l2out = sortByAnagrams(l2)

    assertion.equals(True, abs(l1out.index('ar') - l1out.index('ra')) == 1)
    assertion.equals(True, abs(l1out.index('abc') - l1out.index('cab')) == 1)
    assertion.equals(True, abs(l1out.index('abcxyz') - l1out.index('xzabcy')) == 1)


    assertion.equals(True, abs(l2out.index('ab') - l2out.index('ba')) == 1)
    assertion.equals(True, abs(l2out.index('rt') - l2out.index('tr')) == 1)
    assertion.equals(True, abs(l2out.index('cab') - l2out.index('bca')) == 1)
    assertion.equals(True, abs(l2out.index('qwer') - l2out.index('qwre')) == 1)
    print(l2out)

if __name__ == '__main__':
    main()
