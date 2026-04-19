class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str2={}
        for i in strs:
            val="".join(sorted(i))
            if val not in str2:
                str2[val]=[]
            str2[val].append(i)
        return list(str2.values())

        