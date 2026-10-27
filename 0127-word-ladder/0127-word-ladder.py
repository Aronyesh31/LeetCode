from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for i in range(len(w)):
                for c in ascii_lowercase:
                    nw = w[:i] + c + w[i + 1:]
                    if nw in words:
                        words.remove(nw)
                        q.append((nw, d + 1))
        return 0
