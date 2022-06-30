def groupAnagrams(strs):
    map_dic=dict()
    for word in strs:
        key="".join(sorted(word))
        map_dic.setdefault(key,[]).append(word)
    return [*map_dic.values()]

groupAnagrams(["eat","tea","tan","ate","nat","bat"])