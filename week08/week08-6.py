class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #arr.sort()
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True