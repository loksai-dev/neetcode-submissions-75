class Solution:
    def isPalindrome(self, s: str) -> bool:

        S = ''.join(c for c in s if c.isalnum()).lower()

        i = 0 
        j = len(S) - 1 

        while i < j:
            if S[i]!= S[j]:
                return False 
            else: 
                i += 1 
                j -= 1 
        return True 



        # while left < right:

        #     while left < right and not s[left].isalnum():
        #         left += 1 

        #     while left < right and not s[right].isalnum():
        #         right -= 1 

        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1 
        #     right -= 1
        
        # return True 


