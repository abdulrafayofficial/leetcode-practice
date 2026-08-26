#Solution:

class Solution:

    def roman_to_int(self,roman_string:str):

        numbers = {
                        'I' : 1,
                        'V' : 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000
                    }
        
        total_sum = 0
        for i in range(len(roman_string)):
            current_char = roman_string[i]
            
            if i+1 < len(roman_string):
                next_char = roman_string[i+1]

                if numbers[current_char]>= numbers[next_char]:
                    total_sum += numbers[current_char]
                    
                else:
                    total_sum -= numbers[current_char] 

            else:
                total_sum += numbers[current_char]

        return total_sum  

p = Solution()    
print(p.roman_to_int('XIV'))