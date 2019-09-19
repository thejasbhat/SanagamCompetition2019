#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    for i in range(d,len(expenditure)):
        print(expenditure[i-d:i], median(expenditure[i-d:i]))
        if expenditure[i] >= 2* median(expenditure[i-d:i]):
            count +=1
    return count
def median(arr):
    length = len(arr)
    arr = sorted(arr)
    if length % 2 == 0:
        return (arr[(length//2)-1]+arr[(length//2)])/2
    else:
        return arr[(length)//2]


nd = input().split()

n = int(nd[0])

d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)
