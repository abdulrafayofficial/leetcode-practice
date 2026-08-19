def isPalindrome(x):
    original_string = str(x)
    reversed_string = original_string[::-1]
    return original_string == reversed_string


print(isPalindrome(1121))#false
print(isPalindrome(121))#True



class Solution:
    def isPalindrome(self,x):
        if x < 0 or(x%10 == 0 and x!=0):
            return False
        
        original = x
        reversed_number = 0

        while x>0:
            digit =  x%10
            reversed_number = (reversed_number * 10) + digit
            x = x//10

        return original == reversed_number

result = Solution()
print(result.isPalindrome(12198))



