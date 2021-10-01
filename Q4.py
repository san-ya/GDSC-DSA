# https://practice.geeksforgeeks.org/problems/reverse-an-array/0#

T = int(input())
for iteration in range(T):
    N = int(input())
    A = list(map(int, input().strip().split()))[:N]
    A.reverse()
    # print(' '.join(str(i) for i in A))
    for num in A:
        if A.index(num) == len(A) - 1:
            print(num)
        else:
            print(num, end=" ")