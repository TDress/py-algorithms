from lib import assertion

def compress(S):
    if len(S) == 0:
        raise ValueError('arg `S` must not be empty')

    count_global, count_run = 0, 1
    compressed, char = [], S[0]
    i = 1
    while i < len(S):
        while i < len(S) and S[i] == char:
            count_run += 1; i += 1

        if char is not None:
            compressed.append(char + str(count_run))
            count_global += 2
            if count_global > len(S):
                return S
        if i < len(S):
            char = S[i]
        count_run = 0

    return ''.join(compressed)

def main():
    s = 'aabccccdcebb'
    s2 = 'abbbbbddeeeeg'
    assertion.equals('aabccccdcebb', compress(s))
    assertion.equals('a1b5d2e4g1', compress(s2))


if __name__ == '__main__':
    main()
