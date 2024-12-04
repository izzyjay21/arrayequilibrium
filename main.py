from array import *
def findequilibrium(arr):
    totalsum = sum(arr)
    leftsum = 0
    for i in range(len(arr)):
       rightsum = totalsum - leftsum - arr[i] 
       if rightsum == leftsum:
           return arr[i]
       leftsum += arr[i]
    print("there is no equilibrium")

arr1 =array("i", [100,29,34,45,67,78,9])    
arr2 =array("i", [2,3,5,6,8,2])
 
print(findequilibrium(arr2)) 