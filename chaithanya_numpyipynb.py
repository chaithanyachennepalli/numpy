# -*- coding: utf-8 -*-
"""chaithanya-numpyipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1geOiysm97oDRZwRays-as_LcuzPP6Bfv

**11/09/2023(MONDAY)
C.Chaithanya Reddy
# 20221BCA0301
"""

!python --version

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

x=[2]
print(x,type(x))

x=[2]
print(x,type(x))

x='ch'
print(x,type(x))