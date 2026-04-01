'''def firstRepeated(s):
    len1=len(s)
    for i in range(len1):
        count=1
        for j in range(len1):
            if i!=j and s[i]==s[j]:
                count=0
                break
        if count:
            return s[i]


s='abbaccd'
print(firstRepeated(s))'''
'''def RomantoInt(s):
    roman={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total=0
    len1=len(s)
    for i in range(len1):
        if i+1<len1 and roman[s[i]]<roman[s[i+1]]:
            total-=roman[s[i]]
        else:
            total+=roman[s[i]]
    return total
s='MCM'
print(RomantoInt(s))'''
'''def invalidString(s):
    close_str=s.count(')')
    open_str=0
    for i in range(len(s)):
        if open_str==close_str:
            return i
        if s[i]=='(':
            open_str+=1
s=')()('''

def longestCommon(s):
    result=''
    for ch in s:
        if ch


s='geekforgeek'