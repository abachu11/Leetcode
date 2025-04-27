class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs):
        group_dict = defaultdict(list)
        for word in strs:
            count = [0]* 26
            for val in word:
                count[ord(val)-ord('a')] += 1
            group_dict[tuple(count)].append(word)
        return list(group_dict.values())