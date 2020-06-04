length = len #copy the funtion in your code saves time for looking the funtion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = length(s)
        for i in range(n//2):
            s[i], s[-i-1] = s[-i- 1],s[i]
        """
        Do not return anything, modify s in-place instead.
        """
        
