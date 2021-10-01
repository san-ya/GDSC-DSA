# https://practice.geeksforgeeks.org/problems/find-immediate-smaller-than-x/1/#

class Solution:
    def immediateSmaller(self,arr,n,x):
        if min(arr) >= x:
            return -1
        
        distance = 1
        while distance > 0:
            if x - distance in arr:
                return x - distance
            distance += 1

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.immediateSmaller(arr,n,x)
        print(ans)