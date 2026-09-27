class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []
        for i in s:
            i = i.lower()
            if i.isalnum():
                new_list.append(i)
    
        if new_list == new_list[::-1]:
            return True
        return False

        
        