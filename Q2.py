# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1/?category[]=Arrays&category[]=Arrays&difficulty[]=0&page=2&query=category[]Arraysdifficulty[]0page2category[]Arrays#

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        dictionary = {num: arr.count(num) for num in arr}
        if all(frequency == 1 for frequency in dictionary.values()):
            return -1
        return min([arr.index(key) + 1 for key in dictionary.keys() if dictionary[key] > 1])

if __name__=='__main__':
    t=int(input())
    for _ in range(t):        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))



# METHOD 2

    # if list(set(arr)) == arr:
    #     return -1
    # else:
    #     minimum = n
    #     for num in set(arr):
    #         if arr.count(num) > 1 and arr.index(num) + 1 < minimum:
    #             minimum = arr.index(num) + 1
        
    # return minimum