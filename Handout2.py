## November 2019
## EE2702 Computer Science and Programming, City, University of London 
## The code provided below presents solutions to problems from Handout 2.
## These solutions are not the only possible solutions. 

## Problem 1. 

##def diagonalDifference(arr):
##    # Write your code here
##
##    left_to_right, right_to_left = 0,0
##    for i in range (0, len(arr)):
##        left_to_right=left_to_right+arr[i][i]
##        right_to_left=right_to_left+arr[i][len(arr)-1-i]
##    
##    return abs(left_to_right-right_to_left)
##
##
##f=open('square.txt', 'r+')
##arr=[]
##for line in f:
##    arr.append([float(x) for x in line.split()])
##
##print(diagonalDifference(arr))


####

## Problem 2

##def plusMinus(arr):
##    
##    pos, neg = 0,0
##    for i in arr:
##        if i<0:
##            neg=neg+1
##        elif i>0:
##            pos=pos+1
##
##    print(pos/len(arr))
##    print(neg/len(arr))
##    print((len(arr)-pos-neg)/len(arr))
##
##
##arr = [1, 1, 0, -1, -1]
##
##print(arr)
##plusMinus(arr)

## Problem 3.
## Please note the input and the output. Try to enter more than five numbers 

##lst = list(map(int,input("\nEnter the numbers : ").strip().split()))[:5] 
##x = sum(lst)
##print ("min equals ",(x-(max(lst))), "max equals ",(x-(min(lst))))


## Problem 4. 


##for i in range(1, 5):
##        print(str('#'*i).rjust(4))


## Problem 5

##f=open('results.txt', 'r+')
##results=[]
##for line in f:
##    results.append([float(x) for x in line.split()])

## the very slow way of finding the minimum:

##index_min = 0
##smallest=results[3][0]
##for i in range (1, 50):
##    if results[3][i]<smallest:
##        index_min=i
##        smallest=results[3][0]

## This can be done in Python in a different way, using numpy library:

##import numpy as np
##index_min = np.argmin(results[3])
##
##print("the date and time of the smallest value of the experiments are: ", results[1][index_min], results[2][index_min])
##
