import collections
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dict_ = collections.defaultdict(int)
        for h in range(len(words)):
            dict_[words[h]] = h
        result = []
        for i in range(len(words)):
            word = words[i]
            if "" in dict_ and dict_[""] != i and word == word[::-1]:
                result.append([i,dict_[""]])
            for j in range(len(word)):
                prefix = word[:j+1]
                suffix = word[j+1:]
                if prefix[::-1] in dict_ and dict_[prefix[::-1]] != i and suffix == suffix[::-1]:
                    result.append([i,dict_[prefix[::-1]]])
                if suffix[::-1] in dict_ and dict_[suffix[::-1]] != i and prefix == prefix[::-1]:
                    result.append([dict_[suffix[::-1]],i])
        return(result)