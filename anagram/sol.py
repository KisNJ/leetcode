def isAnagram(s,t) -> bool:
    if sorted(t)==sorted(s):
        return True
    else:
        return False
isAnagram("anagram","nagaram")