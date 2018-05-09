from lib import assertion

def flip_to_win(n):
    is_flipped = longest = run = 0
    last_off, mask = None, 1

    for count in range(31):
        if mask & n:
            run += 1
        elif not is_flipped:
            last_off, is_flipped = count, 1
            run += 1
        else:
            longest = max(longest, run)
            run = count - last_off
            last_off = count

        mask <<= 1

    return max(longest, run)

def main():
    n1 = 15 # 1111
    n2 = 90 # 10011010
    n3 = 0
    n4 = 1775 # 110 1110 1111

    assertion.equals(5, flip_to_win(n1))
    assertion.equals(4, flip_to_win(n2))
    assertion.equals(1, flip_to_win(n3))
    assertion.equals(8, flip_to_win(n4))

if __name__ == '__main__':
    main()
