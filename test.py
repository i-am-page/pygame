def strStr(haystack, needle):
        for i in range(len(haystack)):
            #print("???: ",haystack[i], needle[0], haystack[i:i+len(needle)])
            if haystack[i] == needle[0] and haystack[i : i + len(needle)] == needle:
                #print(i)
                return i
        return -1


print(strStr("sadbutsad", "sad"))
#print(strStr("leetcode","leeto"))
