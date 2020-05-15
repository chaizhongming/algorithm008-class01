#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return 0
        all_com_dict=defaultdict(list)
        L=len(beginWord)
        for i in range(L):
            for word in wordList:
                all_com_dict[word[:i]+"*"+word[i+1:]].append(word)
        queue=collections.deque([(beginWord,1)])
        visited=set()
        while queue:
            current_word,level=queue.popleft()
            for i in range(L):
                intermediate_word=current_word[:i]+"*"+current_word[i+1:]
                for word in all_com_dict[intermediate_word]:
                    if word==endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word,level+1))
        return 0
# @lc code=end

