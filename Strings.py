from typing import List



#1 Reverse string
silver = ["h","e","l","l","o"]


def reverseString(s: List[str]) -> None:
    doi,lens = 0,len(s)
    for x in range(lens):
        s.insert(0,s[doi])
        doi += 2
    del s[lens:]


#2 Reverse interger

intes = -123

def reverseInt(x: int) -> int:
    int_max,int_min = 2147483647,-2147483648
    if x >0:
     rev=  int((str(x)[::-1]))
    else:
     rev= -int((str(-x)[::-1]))

    if rev > int_max or rev < int_min:
        return 0
    return rev



#3 First unique character
s = "leetcode"


def firstUniqChar(s: str) -> int:
    for j in range(len(s)):
        if s[j] in s.replace(s[j], "", 1):
            continue
        else:
            return s[j]
    return -1

#4 Is Anagram valid?

s,t = "anagram" , "nagaram"

def isAnagram(s: str, t: str) -> bool:
    if len(s) > len(t) or len(s) < len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    return False





#5 is Palindrome


s = "0P"


def isPalindrome(s: str) -> bool:
    ss = s
    ss = ss.replace(' ','').lower()
    ss = ''.join([i for i in ss if i.isalpha()])
    forwards,backwards = 0,-1
    if len(ss) == 1:
        return False
    print(ss)
    while forwards < int(len(ss) / 2):
        print(ss[forwards])
        print(ss[backwards])
        if ss[forwards] != ss[backwards]:
            print('False')
            return False
        forwards += 1
        backwards -= 1
    print('True')
    return True


isPalindrome(s)
