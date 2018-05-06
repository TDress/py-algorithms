from lib import assertion

def is1EditAway(S1, S2):
    i = j = edits = 0

    while i < len(S1) or j < len(S2):
        if i < len(S1) and j < len(S2) and S1[i] == S2[j]:
            i += 1; j += 1
        else:
            edits += 1
            if edits > 1:
                return False

            if j == len(S2) or (i + 1 < len(S1) and S1[i + 1] == S2[j]):
                i += 1
            elif i == len(S1) or (j + 1 < len(S2) and S2[j + 1] == S1[i]):
                j += 1
            else:
                i += 1; j += 1

    return True

def main():
    S1, S2 = "hello", "hele"
    assertion.equals(False, is1EditAway(S1, S2))
    S1, S2 = "hello", "helo"
    assertion.equals(True, is1EditAway(S1, S2))
    S1, S2 = "helro", "hello"
    assertion.equals(True, is1EditAway(S1, S2))
    S1, S2 = "hello", "helllo"
    assertion.equals(True, is1EditAway(S1, S2))
    S1, S2 = "hello", "aello"
    assertion.equals(True, is1EditAway(S1, S2))

if __name__ == '__main__':
    main()


