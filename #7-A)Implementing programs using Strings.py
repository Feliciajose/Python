#7-A)Implementing programs using Strings.
def fnReverse(s):
    return s[::-1]
def fnPalindrome(s):
    if(s==s[::-1]):
        return "String is a palindrome"
    else:
        return "String is not a palindrome"

def fnCharcount(s):
charcount = 0
for ch in s:
    if(ch.isalpha()):
        charcount+=1
        return charcount
def fnReplace(s,ss,rs):
if(ss in s):
    return s.replace(ss,rs)
else:
    return "Search string not found. Cannot replace"

S = input("Enter string : ")
print("Reverse of the string : ",fnReverse(S))
print("Palindrome check : ")
print(fnPalindrome(S))
print("Character count =",fnCharcount(S))
searchstr = input("Enter search string : ")
replacestr = input("Enter string to replace : ")
print("Replaced string :")

print(fnReplace(S,searchstr,replacestr))