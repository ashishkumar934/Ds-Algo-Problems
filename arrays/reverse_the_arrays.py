"""
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

Given an array (or string), the task is to reverse the array/string.
"""

## Done

def reverseWord(s):
  output=s[::-1]
  return output

if __name__=='__main__':
  t=int(input())
  while (t>0):
    s=input()
    print(reverseWord(s))
    t=t-1

