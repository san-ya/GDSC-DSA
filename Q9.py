# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1


class Solution:
    def leaders(self, A, N):
        flag = 0
        li = []
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] < A[j]:
                    flag = 1
            if flag == 0:
                li.append(A[i])
            flag = 0
        
        li.append(A[-1])
        
        return li

import math

def main():
    
    T=int(input())
    
    while(T>0):

        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()