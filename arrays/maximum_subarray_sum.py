"""
https://www.codingninjas.com/studio/problems/maximum-subarray-sum_630526?onboarding=true&leftPanelTab=0
"""

from os import *
from sys import *
from collections import *
from math import *


from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    max_sum=0
    current_sum=0
    for i in range(0,len(arr)):
        current_sum+=arr[i]
        if current_sum>=0:
            pass
        else:
            current_sum=0
        max_sum=max(max_sum,current_sum)
    return max_sum

#taking inpit using fast I/O
def takeInput() :
	
    n =  print(input())
    print(n)

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
