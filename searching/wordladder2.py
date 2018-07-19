from lib import assertion

# wordladder 2 on leetcode

def _isDiffByOne(word1, word2):
    if len(word1) != len(word2):
        return False
    diffcnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diffcnt += 1

    return diffcnt == 1

def _transform(word, endWord, words, path, paths):
    if word == endWord:
        if not len(paths) or len(paths[0]) > len(path):
            paths.clear()
            paths.append(path[:])
        elif len(paths[0]) == len(path):
            paths.append(path[:])
    else:
        for w in list(words):
            if _isDiffByOne(word, w):
                words.remove(w)
                path.append(w)
                _transform(w, endWord, words, path, paths)
                path.remove(w)
                words.add(w)


def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    res, words = [], set(wordList)
    _transform(beginWord, endWord, words, [beginWord], res)

    return res


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    assertion.equals(5, len(findLadders(beginWord, endWord, wordList)[0]))

if __name__ == '__main__':
    main()
