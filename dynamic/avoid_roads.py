from lib import assertion

# check out problem statement at https://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709

def avoid_roads(w, h, bad):
    # we care about each corner, so we need to add 1 to height and 1 to width to represent
    # each corner as a cell in a matrix.
    R, C = h + 1, w + 1
    dp = [[0] * C for _ in range(R)]
    
    # we want to use rows and columns, so we need to do a translation of coordinates
    def translate_coords(coords):
        return (abs(int(coords[1]) - (R - 1)), int(coords[0]))

    # check for an untraversable path  ending at end coordinates and starting at the end coords

    def is_untraversable(start, end):
        return (start in bad_starts and end in bad_ends)

    bad_starts_original = list(coords.split()[:2] for coords in bad)
    bad_ends_original = list(coords.split()[2:] for coords in bad)
    bad_starts = set(map(translate_coords, bad_starts_original))
    bad_ends = set(map(translate_coords, bad_ends_original))

    # first row goes first, with first cell always a 1 to start
    dp[R - 1][0] = 1
    for c in range(1, C):
        if dp[R - 1][c - 1] != 0 and not is_untraversable((R - 1, c - 1), (R - 1, c)):
            dp[R - 1][c] = 1

    for r in range(R - 2, -1, -1):
        for c in range(C):
            left_paths = right_paths = 0
            if c > 0 and not is_untraversable((r, c - 1), (r, c)):
                left_paths = dp[r][c - 1]
            if r + 1 < R and not is_untraversable((r + 1, c), (r, c)):
                right_paths = dp[r + 1][c]
            dp[r][c] = left_paths + right_paths

    return dp[0][C - 1]





def main():
    assertion.equals(252, avoid_roads(6,6,["0 0 0 1", "5 6 6 6"]))
    assertion.equals(2, avoid_roads(1,1,[]))
    assertion.equals(6406484391866534976, avoid_roads(35,31, []))
    assertion.equals(0, avoid_roads(2, 2, ["0 0 1 0", "1 2 2 2", "1 1 2 1"]))

if __name__ == '__main__':
    main()
